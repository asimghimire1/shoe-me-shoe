"""
URL configuration for showmeshoe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# showmeshoe/urls.py

from django.contrib import admin
from django.urls import path, include
from accounts.views import signup, login_view, home , logout_view ,index

# showmeshoe/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('accounts/', include('accounts.urls', namespace='accounts')),# Logout URL
]