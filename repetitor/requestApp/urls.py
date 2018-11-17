from django.urls import path
from .views import *


urlpatterns = [
    path('', info, name='url_info'),
    path('contacts/', contacts, name='url_contacts'),
    path('reviews/', reviews, name='url_reviews'),
    path("studentform/", student_form, name='url_student_form')

]
