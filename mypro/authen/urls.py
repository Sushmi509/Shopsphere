from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_,name='login'),
    path('reg',views.register,name='register'),
    path('logout',views.logout_,name='logout'),
    path('profile',views.profile,name='profile'),
]

