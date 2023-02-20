from django.urls import path
from . import views

urlpatterns = [
    path('', views.button_form, name='button_form')
]