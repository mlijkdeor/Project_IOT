from django.urls import path
from . import views
from .forms import LogInForm
from django.contrib.auth import views as auth_views

app_name='core'

urlpatterns=[
    path('', views.index , name='index'),
    path('signup/', views.signup , name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LogInForm), name='login'),

]