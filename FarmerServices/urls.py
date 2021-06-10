"""FarmerServices URL Configuration

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
from django.urls import path
from django.conf import settings
from farmer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name="contact"),
    path('crops/',views.crops,name='crops'),
    path('pestisides/',views.pestisides,name="pestisides"),
    path('about/',views.about,name='about'),
    path('paddy/',views.paddy,name='paddy'),
    path('brinjal/',views.brinjal,name='brinjal'),
    path('sugarcane/',views.sugarcane,name='sugarcane'),
    path('tomato/',views.tomato,name='tomato'),
    path('watermelon',views.watermelon,name='watermelon'),
    path('workers/',views.workers,name='workers'),
    path('users/',views.users,name='users')
]
