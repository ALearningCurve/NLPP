from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

import misaka

from django.contrib.auth import get_user_model
from groups.models import Group

from datetime import date
import json
User = get_user_model()



# These are for the actual post that a person makes and can interact with
class Post(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(User, related_name="post_creator", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    description = models.TextField(blank=True, default="", max_length=8000)
    body_text = models.TextField(blank=True, default="", max_length=8000)

    # might be unecesary
    #users = models.ManyToManyField(User,through="PostMembers")


    creation_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()

    # defualt=2 sets the translation from english to english
    from_lang = models.ForeignKey('SupportedLanguages', related_name="from_langs", on_delete=models.CASCADE)
    to_lang = models.ForeignKey('SupportedLanguages', related_name="to_langs", on_delete=models.CASCADE, default=2)

    def save(self, *args, **kwargs):
        self.body_text = misaka.html(self.body_text)

        is_new = not self.pk        # Checks if the object has been made before to get assin all of the users
        super().save(*args, **kwargs)

        # Generates new PostMembers to track completion of post
        if is_new:
            for member in self.group.members.all():
                post_mem = PostMembers(
                    id=None,
                    post=self,
                    user=member,
                    has_completed_work=False,
                    completion_date=date(2005, 7, 27),
                )
                post_mem.save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("groups:posts:single", kwargs={"pk": self.pk, 'slug':self.group.slug})


    class Meta:
        ordering = ["-creation_date"]



class SupportedLanguages(models.Model):
    code = models.CharField(max_length=2, unique=True, null=False)
    ISO639_1 = models.CharField(max_length=5, unique=True, null=False)
    name = models.CharField(max_length=15, unique=True, null=True)

    def __str__(self):
        return self.name

# Stores the information of whatthe user has done with the post such as what words they clicked on,
# How many times they clicked on each word (and perhaps time spent on the post)
class PostMemberInteractionInformation(models.Model):
    post_member = models.OneToOneField('PostMembers', related_name='post_info', on_delete=models.CASCADE, null=True)

    '''
    These click fields are actualy stringified JSONS that are being handled by JSONHandler.add_value()
    the jsons will look like the following where "number" is the amount of times clicked and ["word"]
    is the word that was clicked "number" times
    data = {
        "1": ["uno", "single", "one"],
        "2": ["dos", "double", "two"],
        "3": ["tres", "triple", "three"]
        }

        {"1":[],}
    '''
    # Keeps track of the single clicks in the double click modal
    # This should be the synomyns
    single_clicks = models.TextField()
    # Keeps track of the double clicks in the double click modal
    # This should be the definitions
    double_clicks = models.TextField()

    def __str__(self):
        return self.post_member.user.username + " info"



# This keeps track of who has done what on each post
# This includes the user, when the work was completed,
# if it was completed, and has a one to many relationship with
# UserPostInteractionInformation as the target

class PostMembers(models.Model):
    post = models.ForeignKey(Post,related_name='post_asignees',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='posts_assigned',on_delete=models.CASCADE)

    has_completed_work = models.BooleanField(default=False)
    completion_date = models.DateTimeField()


    def save(self, *args, **kwargs):
        is_new = not self.pk        # Checks if the object has been made before to get assin all of the users
        super().save(*args, **kwargs)
        # Generates new PostMembersInfo to track completion of post
        if is_new:
            post_info = PostMemberInteractionInformation(
                post_member = self,
                single_clicks = json.dumps( {"1":[],} ),
                double_clicks = json.dumps( {"1":[],} ),
            )
            post_info.save()

    def __str__(self):
        return  self.post.name + " : " +  self.user.username + " : " + str(self.has_completed_work)

    class Meta:
        unique_together = ("post", "user")
