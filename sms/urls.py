from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receive_sms/', views.receive_sms, name='receive_sms')
]