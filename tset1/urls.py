"""te2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from users.views import ximport, send_mails, home, logout, send_mails_ii, cancel_inform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ximport/', ximport, name='ximport'),
    path('send_mails/', send_mails, name='send_mails'),
    path('send_mails_ii/', send_mails_ii, name='send_mails_ii'),
    path('', home, name='home'),
    path('cancel_inform', cancel_inform, name='cancel_inform'),
    path('logout/', logout, name='logout'),
]
