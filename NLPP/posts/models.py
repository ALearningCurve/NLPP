from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


from django.contrib.auth import get_user_model
from groups.models import Group
User = get_user_model()


# These are for the actual post that a person makes and can interact with
class Post(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(User, related_name="post_creator", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)    

    description = models.TextField(blank=True, default='', max_length=8000)
    body_text = models.TextField(blank=True, default='', max_length=8000)

    users = models.ManyToManyField(User,through="PostMembers")
    creation_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"pk": self.pk})


    class Meta:
        ordering = ["-creation_date"]



# This keeps track of who is who
class PostMembers(models.Model):
    post = models.ForeignKey(Post,related_name='post',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_posts',on_delete=models.CASCADE)
    completion_date = models.DateTimeField()



    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("post", "user")
