
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

# What is render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.views import generic
from groups.models import Group, GroupMember
from . import models

from django.db import IntegrityError
from django.contrib import messages

from django.http import HttpResponseRedirect
from .forms import GroupForm, GroupFindForm




# Shows the details of one specific group (ie all of the readings/videos)
class SingleGroup(LoginRequiredMixin, generic.DetailView):
    model = Group


#Lists groups that the user is in
class ListGroups(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'groups/group_list.html'



# Some actions performed to add the user to the GroupMember
class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)




#Some action performed to remove the user from the group
class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        return super().get(request, *args, **kwargs)


# Action to remove a user form a given group
class KickUserGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.kwargs.get("pk"),
                group__slug=self.kwargs.get("slug")
            ).get()

            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        return super().get(request, *args, **kwargs)



def group_find(request):
    form = GroupFindForm()

    if request.method == "POST":
        form = GroupFindForm(request.POST)
        if form.is_valid():
            find_slug = form.cleaned_data['slug']

            try:
                group = Group.objects.get(slug=find_slug)
                return HttpResponseRedirect(reverse("groups:single", kwargs={"slug": find_slug}))
            except ObjectDoesNotExist:

                return render(request,'groups/group_find_form.html',{'form':form, 'valid':False})


    return render(request,'groups/group_find_form.html',{'form':form, 'valid':True})

###########
# Views Restricted to the original owner
###########

# TODO Make a new instance & assign the author of the class
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Group

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

# TODO Update
class UpdateGroup(LoginRequiredMixin, generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'groups/about.html'
    form_class = GroupForm
    model = Group

# TODO Some action to delete the view given owner
class DeleteGroup(LoginRequiredMixin, generic.DeleteView):
    model = Group

    template_name = "groups/group_confirm_delete.html"


    def get_success_url(self):
        return reverse("groups:all")
    # def delete(self, *args, **kwargs):
    #     messages.success(self.request, "Group Deleted")
    #     return super().delete(*args, **kwargs)
