from django.urls import path
from posts.views import index,about,service,create_post

urlpatterns = [
    path('',index,name='post_home'),
    path('about',about,name='post_about'),
    path('services',service,name='post_service'),
    path('create-post',create_post,name='create_post'),
]