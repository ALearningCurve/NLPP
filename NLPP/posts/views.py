from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
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
from . import models
from . import textExtractor as out

from groups.models import Group



# from django.contrib.auth import get_user_model
# User = get_user_model()
#
#
# class PostList(LoginRequiredMixin, generic.ListView):
#     model = models.Post
#
#
#
# class UserPosts(generic.ListView):
#     model = models.Post
#     template_name = "posts/user_post_list.html"
#
#     def get_queryset(self):
#         try:
#             self.post_user = User.objects.prefetch_related("posts").get(
#                 username__iexact=self.kwargs.get("username")
#             )
#         except User.DoesNotExist:
#             raise Http404
#         else:
#             return self.post_user.posts.all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post_user"] = self.post_user
#         return context
#
#
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
#
#
# class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
#     model = models.Post
#     select_related = ("user", "group")
#     success_url = reverse_lazy("posts:all")
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user_id=self.request.user.id)
#
#     def delete(self, *args, **kwargs):
#         messages.success(self.request, "Post Deleted")
#         return super().delete(*args, **kwargs)


# this function returns a json file containing the translation
# https://stackoverflow.com/questions/51106830/how-to-call-python-functions-from-javascript-in-django
# That link is how we will integrate this function with the translations, or maybe we will use js
def translate(request):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate?"
    key = "trnsl.1.1.20200117T014254Z.b5ec263d36a25c07.698d2465df9fd59677fe87985d82aa6fef88f8af"
    text = request.POST['text']
    lang = request.POST['lang']



    is_cached = ('trans_'+lang+"_"+text in request.session)

    if not is_cached:
        url = url + "key="+key+"&text="+text+"&lang="+lang
        response = requests.get(url, verify=False)
        request.session['trans_'+lang+"_"+text] = response.json()

    translation = request.session['trans_'+lang+"_"+text]

    # return render(request, 'posts/test.html', {
    #     'text': translation,
    #     'is_cached' : is_cached,
    # })

    return JsonResponse(translation)


# provides dictionary translations for words , only works for english to other language, not the other way around
# def translate(request):
#     url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup?"
#     key = "dict.1.1.20200122T170248Z.de87d85bf55ff34f.1d5d0127e696c6496ff9250a57595d18c38f5abd"
#     text = "hola"
#     lang = "es-en"
#
#
#
#
#     is_cached = ('dict_'+lang+"_"+text in request.session)
#
#     if not is_cached:
#         url = url + "key="+key+"&text="+text+"&lang="+lang
#         response = requests.get(url, verify=False)
#         request.session['dict_'+lang+"_"+text] = response.json()
#
#     translation = request.session['dict_'+lang+"_"+text]
#
#
#     return render(request, 'posts/test.html', {
#
#         'text': translation,
#         'is_cached' : is_cached,
#     })


@xframe_options_sameorigin
def file_upload(request, slug):
    return HttpResponse(out.convertToText(request.FILES['file'],"english"))
