from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import CreateBlogPostForm
from account.forms import AccountUpdateForm
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from blog.models import BlogPost
from account.models import Account
from django.db.models import Q
# Create your views here.


def blog_view(request):
    context = {}
    blog = BlogPost.objects.all()
    context['blog']=blog
    return render(request, 'blog/blog.html', context)


def create_blog_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, 'blog/create_blog.html', context)


def blog_post_detail(request):

    if not request.user.is_authenticated:
        return redirect("account:login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=request.user)
    context['blog_posts'] = blog_posts

    return render(request, "blog/blogPostDetail.html", context)


def detail_blog_view(request, slug):

    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'blog/detail_blog.html', context)


# def edit_blog_view(request, slug):

#     context = {}
#     user = request.user
#     if not user.is_authenticated:
#         return redirect('must_authenticate')

#     blog_post = get_object_or_404(BlogPost, slug=slug)
#     if request.POST:
#         form = UpdateBlogPostForm(
#             request.POST or None, request.FILES or None, instance=blog_post)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#             context['success_message'] = "Updated"
#             blog_post = obj

#     form = UpdateBlogPostForm(
#         initial={
#             "title": blog_post.title,
#             "body": blog_post.body,
#             "image": blog_post.image,
#         }
#     )
#     context['form'] = form

#     return render(request, 'blog/edit_blog.html', context)


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.filter(
            Q(title__contains=q) |
            Q(body__icontains=q)
        ).distinct()
        for post in posts:
            queryset.append(post)

    # create unique set and then convert to list
    return list(set(queryset))
