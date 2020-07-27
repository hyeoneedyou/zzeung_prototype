"""zzeung_prototype URL Configuration

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
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import main
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('english/', include('english.urls')),
    path('accounting/', include('accounting.urls')),
    path('board/', include('board.urls')),
    path('chinese/', include('chinese.urls')),
    path('computer/', include('computer.urls')),
    path('hoteltour/', include('hoteltour.urls')),
    path('japanese/', include('japanese.urls')),
    path('trade/', include('trade.urls')),
    path('accounts/', include('allauth.urls')),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
