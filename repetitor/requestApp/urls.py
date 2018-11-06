from django.urls import path
from .views import *


urlpatterns = [
<<<<<<< HEAD
    path('', info, name='url_info'),
    path('contacts/', contacts, name='url_contacts'),
    path('reviews/', reviews, name='url_reviews')
=======
    path('', info, name="courses"),
    path('contacts/', contacts, name="contacts"),
    path('reviews/', reviews, name="reviews")
>>>>>>> master
]
