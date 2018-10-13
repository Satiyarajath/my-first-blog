from django.shortcuts import render

# Create your views here.
def Post_List(request):
    return render(request,'blog/Post_List.html', {}) 