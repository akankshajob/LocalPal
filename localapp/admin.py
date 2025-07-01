from django.contrib import admin
from .models import Facility, UserProfile, Feedback  # adjust with your actual models
from django.contrib import admin
from .models import UserProfile
from .models import Facility, Feedback


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username', 'phone', 'address')

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Facility)
admin.site.register(Feedback)

