from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
from posts.forms import PostCreationForm
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.views import View
from django.core.paginator import Paginator
from django.utils.decorators import  method_decorator
# Create your views here.
# def index(request:HttpRequest):
#     posts = Post.objects.all()
#     context = {'posts':posts}
#     return render(request,template_name='index.html',context=context)

class HomePage(View):
    template_name = 'index.html'
    def get(self,request):
        posts = Post.objects.all()
        paginator = Paginator(posts,3)
        page_number = self.request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {'posts':page}
        return render(request,self.template_name,context=context)

class AboutPage(HomePage):
    template_name='about.html'


def service(request:HttpRequest):
    return render(request,template_name='services.html')

# @login_required
# def create_post(request:HttpRequest):
#     form=PostCreationForm()
#     if request.method == "POST":
#         form=PostCreationForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('create_post')
#     context = {
#         'form':form
#     }
#     return render(request,'createpost.html',context)

@method_decorator(login_required,'dispatch')
class CreatePostView(View):
    template_name='createpost.html'
    form_class=PostCreationForm
    initial_values={"key":"value"}

    def get(self,request):
        form=self.form_class(initial=self.initial_values)

        context={
            "form":form
        }

        return render(request,'createpost.html',context)
    
    def post(self,request):
        form=self.form_class(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect('post_home')



def post_detail(request:HttpRequest,post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post':post}
    return render(request,'post_detail.html',context)

@login_required
def update_post(request:HttpRequest,post_id):
    post = Post.objects.get(pk=post_id)
    form = PostCreationForm(instance=post)
    if request.method =='POST':
        form = PostCreationForm(instance=post,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('post_home')
    context = {'form':form}
    return render(request,'update_post.html',context)