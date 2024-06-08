"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import app.views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index/index.html")),
    path('admin/', admin.site.urls),
    path('map/', app.views.map),
    path('restaurant/', app.views.restaurant),
    path('comments/', app.views.comments),
    path('compile/', app.views.compile),
    path('login/', app.views.login),
    path('signup/', app.views.signup),
    path('signup/add/', app.views.signupadd),
    path('userlist/', app.views.userlist),
]
