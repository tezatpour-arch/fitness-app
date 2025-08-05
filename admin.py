from django.contrib import admin
from .models import UserProfile, WorkoutProgram, ContactMessage

# ثبت WorkoutProgram بدون دکوریتور
admin.site.register(WorkoutProgram)

# ثبت UserProfile با دکوریتور
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fitness_level')
    list_filter = ('fitness_level',)
    search_fields = ('user__username', 'user__email')
    ordering = ('user',)

# ثبت ContactMessage با دکوریتور
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    ordering = ('-created_at',)
