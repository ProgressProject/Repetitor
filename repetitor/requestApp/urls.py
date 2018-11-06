from django.urls import path
from .views import *


urlpatterns = [
    path('', info, name="courses"),
    path('contacts/', contacts, name="contacts"),
    path('reviews/', reviews, name="reviews")
]
