from django.shortcuts import render
from service.models import Service
from homepage.models import welcome
# Create your views here.
def service_view(request):
    context = {}
    service = Service.objects.all()
    well = welcome.objects.all()
    context['service']=service
    context['well']=well
    return render(request, 'service/service.html', context)