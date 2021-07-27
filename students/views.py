from django.shortcuts import render
from students.models import Students
# Create your views here.
def students_view(request):
    context = {}
    student = Students.objects.all()
    context['student'] = student
    return render (request, 'students/students.html', context)