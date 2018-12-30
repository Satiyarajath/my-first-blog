from django.contrib import admin

# Register your models here.
from .models import Post,Comment            # import your prev created models

admin.site.register(Post)           # register you Post Model to show in admin page
admin.site.register(Comment)        # register you Comment Model to show in admin page
