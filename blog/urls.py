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
]
