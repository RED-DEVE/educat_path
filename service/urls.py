from django.urls import path
from service.views import (
    service_view
)

app_name = 'service'

urlpatterns =[
    path('serv/', service_view, name='HomeService'),
]