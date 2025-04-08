from django.contrib import admin
from .models import UserProfile, Post, ImageUpload  # Import your models

# Register your models here
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(ImageUpload)
