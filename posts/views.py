from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
from posts.forms import PostCreationForm
from posts.models import Post

# Create your views here.
def index(request:HttpRequest):
    return render(request,template_name='index.html')

def about(request:HttpRequest):
    return render(request,template_name='about.html')

def service(request:HttpRequest):
    return render(request,template_name='services.html')

def create_post(request:HttpRequest):
    form=PostCreationForm()
    if request.method == "POST":
        data = request.POST
        post = Post.objects.create(
            title = data['title'],
            content = data['content'],
            author = data['author'],
        )
        return redirect('create_post')
    context = {
        'form':form
    }
    return render(request,'createpost.html',context)