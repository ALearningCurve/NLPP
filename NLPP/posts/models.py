from django.db import models

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


from django.contrib.auth import get_user_model
User = get_user_model()


# These are for the actual post that a person makes and can interact with
class Post(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    creator = models.ForeignKey(User, related_name="group_owners", on_delete=models.CASCADE)
    description = models.TextField(blank=True, default='')

    users = models.ManyToManyField(User,through="PostMembers")

    creation_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=True)

    models.ForeignKey(PostType,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["-creation_date"]

# These are for the catagories of the post, prob only 3 max: Text, Image, and Video
class PostType(models.Model):
    type_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.top_name

# This keeps track of who is who
class PostMembers(models.Model):
    post = models.ForeignKey(Post,related_name='posts',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_posts',on_delete=models.CASCADE)
    completion_date = models.DateTimeField()

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("post", "user")
