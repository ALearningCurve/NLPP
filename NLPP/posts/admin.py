from django.contrib import admin
from . import models

# Register your models here.
class PostMemberInline(admin.TabularInline):
    model = models.PostMembers

class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostMemberInline,
    ]

class PostMemberInteractionInformationInline(admin.TabularInline):
    model = models.PostMemberInteractionInformation

class PostMembersAdmin(admin.ModelAdmin):
    inlines = [
        PostMemberInteractionInformationInline,
    ]
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.SupportedLanguages)
admin.site.register(models.PostMembers, PostMembersAdmin)
admin.site.register(models.PostMemberInteractionInformation)
