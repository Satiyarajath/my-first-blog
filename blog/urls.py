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
    path('post/<int:pk>/edit/',views.Post_Edit, name = 'Post_Edit') # reverse lookup - edit existig post
]
