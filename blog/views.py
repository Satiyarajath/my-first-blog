from django.shortcuts import render, get_object_or_404, redirect   # in case primary key,'pk' doesn't match
from .models import Post                # including models inside view to query the DB
                                        # and send value to template
                                        # . --> current directory

from django.utils import timezone           # to use in query set

from .forms import PostForm                 # to use PostForm in post_new


# Create your views here.
def Post_List(request):
    # query set from DB 
    # all posts less than equal to current time and ordered by created date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    # pass the query set to template
    return render(request,'blog/Post_List.html', {'posts':posts}) 

def Post_Detail(request,pk):
    # query set from DB to get post using primary key
    # get_object_or_404 --> to handle pk doesn't exist
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/Post_Detail.html',{'post' : post})

def Post_New(request):
    # create a form object using PostForm and pass to template
    # scenario 1 --> when form returns with value in "request.POST"
    #                   a. create a form object with values from 'request.POST'
    #                   b. if form is valid,
    #                       1. update necessary fields in post
    #                       2. save post
    #                       3. redirect to post detail
    # scenario 2 --> blank form

    # scenario 1:
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("Post_Detail", pk=post.pk)
    # scenario 2:
    else:
        form = PostForm()
    return render(request,'blog/Post_Edit.html',{'form':form})

def Post_Edit(request,pk):
    # scenario 1 : edited post is returned in request.POST
    #             a. create a form object using request.POST, instance = post
    #             b. validate the form 
    #             c. save post using values from form
    #             d. update other fields in post
    #             e. explicit save of post
    #             f. redirect to detail page
    # scenario 2 : (first time ) send existing post in edit html (instance = post)

    post = get_object_or_404(Post,pk=pk)        # getting the post to be edited using pk

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("Post_Detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/Post_Edit.html',{'form':form})      # template reused