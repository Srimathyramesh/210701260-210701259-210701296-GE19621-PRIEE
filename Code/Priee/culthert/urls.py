from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('signup/profile/',views.profile,name='profile'),
    path('post/',views.post,name='post'),
    path('signup/user/',views.user,name='user')
]
