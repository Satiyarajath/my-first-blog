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

    # methods inside class Post

    # update published date for the post with current date time and save the post
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # returns string of Title when object belonging to Post class is called
    def __str__(self):
        return self.title


    def approved_comments(self):
        return self.comments.filter(approved_comment = True)


class Comment(models.Model):
    # related_name --> to access comment model from inside post model 
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
