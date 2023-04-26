from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('display_data/', views.display_data, name='display_data'),
]