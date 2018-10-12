from django.contrib import admin

# Register your models here.
from .models import Post            # import your prev created model

admin.site.register(Post)           # register you Post Model to show in admin page
