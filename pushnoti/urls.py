"""pushnoti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home.views import *

urlpatterns = [

    path('' , index),
    path('send/' , send),
    path('send_device_id/', send_device_id, name='send_device_id'),
    path('firebase-messaging-sw.js',showFirebaseJS,name="show_firebase_js"),
    path('delete_device_id/', delete_device_id, name='delete_device_id'),
    path('admin/', admin.site.urls),
]
