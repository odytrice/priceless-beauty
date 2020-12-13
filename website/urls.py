from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'website.index'),
    path('skincare', views.skincare, name = 'website.skincare'),
    path('makeup', views.makeup, name = 'website.makeup'),
    path('hair', views.hair, name = 'website.hair')
]