from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

import misaka

from django.contrib.auth import get_user_model
from groups.models import Group

from datetime import date
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
    to_lang = models.ForeignKey('SupportedLanguages', related_name="to_langs", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.body_text = misaka.html(self.body_text)

        is_new = not self.pk        # Checks if the object has been made before to get assin all of the users
        super().save(*args, **kwargs)

        # Generates new PostMembers to track completion of post
        if is_new:
            print("Generating users")

            for member in self.group.members.all():
                print ("Adding: " + member.username)
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



# This keeps track of who is who
class PostMembers(models.Model):
    post = models.ForeignKey(Post,related_name='post_asignees',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='posts_assigned',on_delete=models.CASCADE)

    has_completed_work = models.BooleanField(default=False)
    completion_date = models.DateTimeField()

    

    def __str__(self):
        return self.user.username + " : " + self.post.name

    class Meta:
        unique_together = ("post", "user")

class SupportedLanguages(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=15, unique=True, null=True)

    def __str__(self):
        return self.name
