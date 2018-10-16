from django.shortcuts import render
from .models import Post                # including models inside view to query the DB
                                        # and send value to template
                                        # . --> current directory

from django.utils import timezone           # to use in query set


# Create your views here.
def Post_List(request):
    # query set from DB 
    # all posts less than equal to current time and ordered by created date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    # pass the query set to template
    return render(request,'blog/Post_List.html', {'posts':posts}) 