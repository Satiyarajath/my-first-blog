from django.db import models

# Create your models here.
from django.utils import timezone       # since we need date and time (make sure USE_TZ = True in settings.py)

# creating model 'Post' for application 'blog'

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# update published date for the post with current date time and save the post
def publish(self):
    self.published_date = timezone.now()
    self.save()

# returns string of Title when object belonging to Post class is called
def __str__(self):
    return self.title


