from django.urls import path
from contact.views import Contact_Form

app_name = 'contact'

urlpatterns = [
    path('form/', Contact_Form, name="form"),
]
