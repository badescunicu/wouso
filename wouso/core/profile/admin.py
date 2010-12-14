from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from wouso.core.profile.models import *

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(OldUserAdmin):
    inlines = [ UserProfileInline ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Artifact)
admin.site.register(Message)