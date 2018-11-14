from django.urls import path
from .views import *


urlpatterns = [
    path('', info, name='url_info'),
    path('contacts/', contacts, name='url_contacts'),
    path('reviews/', reviews, name='url_reviews'),
    path('students/', students_list, name='students_list'),

]
