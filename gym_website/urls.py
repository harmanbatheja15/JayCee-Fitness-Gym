from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('gallery', views.gallery, name="gallery"),
    path('free_trial', views.free_trial, name="free_trial"),
    path('group_basic_pricing', views.group_basic_pricing, name="group_basic_pricing"),
    path('group_standard_pricing', views.group_standard_pricing, name="group_standard_pricing"),
    path('group_premium_pricing', views.group_premium_pricing, name="group_premium_pricing"),
    path('personal_basic_pricing', views.personal_basic_pricing, name="personal_basic_pricing"),
    path('personal_standard_pricing', views.personal_standard_pricing, name="personal_standard_pricing"),
    path('personal_premium_pricing', views.personal_premium_pricing, name="personal_premium_pricing"),
    path('about', views.about, name="about"),
]
