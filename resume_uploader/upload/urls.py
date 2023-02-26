from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.ResumeView.as_view(), name='form'),
]    