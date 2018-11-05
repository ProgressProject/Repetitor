from django.urls import path
from .views import *


urlpatterns = [
    path('', info),
    path('contacts/', contacts),
    path('reviews/', reviews)
]
