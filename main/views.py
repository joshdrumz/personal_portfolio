from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import Project
from .forms import ContactForm

# Create your views here.


def homepage(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def projects(request):
    return render(request, 'main/projects.html', context={'project': Project.objects.all})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [
                          'duhhobo@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main:success')
    return render(request, 'main/email.html', {'form': form})


def success(request):
    return render(request, 'main/success.html')
