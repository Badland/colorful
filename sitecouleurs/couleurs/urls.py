from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/',views.userpage,name='userpage'),
    path('<int:user_id>/welcome/',views.welcome,name='welcome'),
    path('<int:user_id>/begin/',views.begin,name='begin'),    url( r'^register/$', views.Register, name='register' ),
    url( r'^login/$', views.Login, name='login' ),
    url( r'^logout/$', views.Logout, name='logout' ),
    ]