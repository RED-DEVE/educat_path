from django.shortcuts import render,redirect
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.





def Contact_Form(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context['success_message'] = "Message Send Successfully"
    form = ContactForm()
    context['form'] = form
    return render(request, 'contact/contact_form.html', context)