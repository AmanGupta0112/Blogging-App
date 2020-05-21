"""myblogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
Rest Framework Api
    To get the status of the post you need to add api/blog/ + the primary key value to the  
"""
from django.contrib import admin
from  django.conf.urls import url,include
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    url(r'accounts/login/$',LoginView.as_view(),name='login'),
    url(r'accounts/logout/$',LogoutView.as_view(),name='logout',kwargs={'next':''}),
    # To access the django api view app api/blog/ and the primary key of the post to check the status that the post is active or not.
    url(r'api/blog/', include('blog.api.urls',namespace = 'blog_api')),
]
