from django.shortcuts import render
from operator import attrgetter
from blog.models import BlogPost
from blog.views import get_blog_queryset
from homepage.models import welcome
from about.models import About
from service.models import Service
from students.models import Students
from comments.models import Comments
from blog.models import BlogPost
# Create your views here.


def home(request):

    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    blog_posts = sorted(get_blog_queryset(
        query), key=attrgetter('date_updated'), reverse=True)
    context['blog_posts'] = blog_posts
    Welcome = welcome.objects.all()
    about = About.objects.all()
    service = Service.objects.all()
    student = Students.objects.all()
    comment = Comments.objects.all()
    blog = BlogPost.objects.all()
    context['about']=about
    context['Welcome']= Welcome
    context['service']=service
    context['student']=student
    context['comment']= comment
    context['blog']= blog

    return render(request, "homepage/home.html", context)
