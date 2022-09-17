from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name='login'),
    path('profile_page',views.profilePg,name='profilePg'),
    path('upload',views.upload,name='upload'),
    path('logout',views.logout,name='logout'),
    path('postf',views.postf,name='postf'),
    path('clogin',views.clogin,name='clogin'),
    path('postit',views.postit,name='postit'),
    
]