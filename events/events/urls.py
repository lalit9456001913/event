"""events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from event import views
from django.contrib.auth import views as auth_views
print('pankaj')
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url('signup',views.signup, name='signup'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url('view1',views.view1,name='view1'),
    url('login', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url('create_event',views.create_event,name='create_event'),
    url('view_event',views.view_event,name='view_event'),
    url('register',views.register,name='register'),
    url('delete',views.delete,name='delete'),
    url('',views.home,name='home'),


]
