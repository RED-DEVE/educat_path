from django.shortcuts import render
from about.models import About, Why,Team
# Create your views here.

def about_view(request):
    context = {}
    about =About.objects.all()
    why = Why.objects.all()
    team = Team.objects.all()
    context['about']=about
    context['why']=why
    context['team']=team
    return render(request,'about/about.html', context)
