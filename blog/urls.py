""" 
URLconf file inside blog application

imports from views.py of blog application

"""

from django.urls import path
from . import views                         # . --> current directory
# same as 
# from blog import views                 

urlpatterns = [
    path('',views.Post_List,name='Post_List'),   # named url - useful for reverse URL mapping
    path('post/<int:pk>/',views.Post_Detail,name='Post_Detail'),   # named url - for reverse lookup of each post
    path('post/new/', views.Post_New, name='Post_New'), # named url - for reverse lookup - new post
    path('post/<int:pk>/edit/',views.Post_Edit, name = 'Post_Edit'), # reverse lookup - edit existig post
    path('post/drafts/',views.Post_Drafts_List, name = 'Post_Drafts_List'), # reverse lookup - drafts list
    path('post/<int:pk>/publish/',views.Post_Publish, name = 'Post_Publish'), # reverse lookup - Publish post
    path('post/<int:pk>/delete/',views.Post_Delete, name = 'Post_Delete'), # reverse lookup - Post Delete
    path('post/<int:pk>/comment/',views.Add_Comment_To_Post, name= 'Add_Comment_To_Post'), # add comment to post
    path('comment/<int:pk>/remove/',views.Comment_Remove, name= 'Comment_Remove'), # comment remove
    path('comment/<int:pk>/approve/',views.Comment_Approve, name= 'Comment_Approve'), # comment approve
]
