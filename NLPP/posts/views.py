from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, JsonResponse
from django.views import generic
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import requests
import json
import os

from . import forms
from . import textExtractor as out
from . import JSONHandler

from . import models
from groups.models import Group



# from django.contrib.auth import get_user_model
# User = get_user_model()

class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = models.Post



class CreatePost(LoginRequiredMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ("name", "description", "body_text", "from_lang","to_lang","due_date")
    model = models.Post


    def get_user_groups(self):
        return get_object_or_404(Group, slug=self.kwargs.get("slug"), creator=self.request.user)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.group = get_object_or_404(Group, slug=self.kwargs.get("slug"))
        self.object.save()
        return super().form_valid(form)

class UpdatePost(LoginRequiredMixin, generic.UpdateView):
    # form_class = forms.PostForm
    fields = ("name", "description", "body_text", "from_lang","to_lang","due_date")
    model = models.Post


    def get_user_groups(self):
        return get_object_or_404(Group, slug=self.kwargs.get("slug"), creator=self.request.user)


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.group = get_object_or_404(Group, slug=self.kwargs.get("slug"))
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = models.Post

    def get_success_url(self):
        return reverse_lazy("groups:single", kwargs={'slug': self.object.group.slug})

    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs)


# this function returns a json file containing the translation
# https://stackoverflow.com/questions/51106830/how-to-call-python-functions-from-javascript-in-django
# That link is how we will integrate this function with the translations, or maybe we will use js
def translate(request):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate?"
    key = "trnsl.1.1.20200117T014254Z.b5ec263d36a25c07.698d2465df9fd59677fe87985d82aa6fef88f8af"
    text = request.POST['text']
    lang = request.POST['lang']
    post_pk = request.POST['post_pk']


    is_cached = ('trans_'+lang+"_"+text in request.session)

    if not is_cached:
        url = url + "key="+key+"&text="+text+"&lang="+lang
        response = requests.get(url, verify=False)
        request.session['trans_'+lang+"_"+text] = response.json()

    translation = request.session['trans_'+lang+"_"+text]

    JSONHandler.update_database(_request = request, _method = JSONHandler.Methods.OneClick, _post_pk = post_pk, _text = text)
    return JsonResponse(translation)


# Uses language processing to convert images or extract from pdfs/word docs
@xframe_options_sameorigin
def file_upload(request, slug):
    return HttpResponse(out.convertToText(request.FILES['file'],"english"))




# Gets the postInfo from the post_pk and post member pk
# Returns a json with the post member info objects information
@login_required
def member_info_detail(request, slug, post_info_pk, method):
    post_info = get_object_or_404(models.PostMemberInteractionInformation,id=post_info_pk)

    # If user is not one the person who made the data or own the post, then return an error
    if(post_info.post_member.user != request.user and post_info.post_member.post.creator != request.user):
        return JsonResponse(JSONHandler.ErrorCodes.r403)
    # Get the json from th e table and return the data or if not found return 404 error
    info = JSONHandler.get_json(_method = method, _info_object = post_info)
    return JsonResponse(info)


# fills out a graph with the provided information
@login_required
def graph(request, slug, post_pk, post_member_pk, method):
    # Checks if the user is the creator, we onle want the creator to see who did what
    # If not the creator then respond with an error
    post = get_object_or_404(models.Post, pk=post_pk)
    if (post.creator != request.user):
        raise Http404("You must be the post creator to see this page")
    return render(request, 'posts/_post_click_graphs.html')

# Simple testing page to see what some functions do,
# and is normally disabled
def test(request, slug):
    return render(request, 'posts/test.html')
