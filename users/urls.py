from django.urls import path
from users.views import login_user,sign_up,logout_user
from django.contrib.auth import views as auth_views
from users.forms import LoginForm
urlpatterns = [
    path('signup/',sign_up,name='sign_up'),
    path('login/',auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form = LoginForm
    ),name='login'),
    path('logout/',logout_user,name='log_out')
]