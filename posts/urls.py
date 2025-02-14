from django.urls import path
from posts.views import HomePage,AboutPage,CreatePostView,service,post_detail,update_post

urlpatterns = [
    path('',HomePage.as_view(),name='post_home'),
    path('about',AboutPage.as_view(),name='post_about'),
    path('services',service,name='post_service'),
    path('create-post',CreatePostView.as_view(),name='create_post'),
    path('post/<int:post_id>',post_detail,name='post_detail'),
    path('post/update/<int:post_id>',update_post,name='update_post'),
]