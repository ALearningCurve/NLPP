from django.contrib import admin
from . import models

# Register your models here.
class PostMemberInline(admin.TabularInline):
    model = models.PostMembers

class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostMemberInline,
    ]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.SupportedLanguages)
