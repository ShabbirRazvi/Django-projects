from django.urls import path
from .views import *

urlpatterns = [
    path('Register/', register_views),
]
