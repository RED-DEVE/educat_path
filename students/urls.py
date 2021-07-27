from django.urls import path
from students.views import (
    students_view,
)

app_name ='students'
urlpatterns =[
    path('students/', students_view, name='student'),
]