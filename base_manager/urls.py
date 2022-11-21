from django.urls import path

from . import views

urlpatterns = [
    path('show_cve/<str:cve_name>/', views.show_cve, name='show_cve'), 
    path('load_cve/', views.load_cve, name='load_cve'), 
    path('show_networkdevice/<str:networkdevice_name>/', views.show_networkdevice, name='show_networkdevice'), 
    path('load_networkdevice/', views.load_networkdevice, name='load_networkdevice'), 
]