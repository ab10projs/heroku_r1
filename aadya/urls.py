from django.urls import path
from aadya import views

urlpatterns = [
    path('poems/', views.poems, name='poems'),
    ]