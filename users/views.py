from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm, SignUpForm


def home(request):
    form = SignUpForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
            "title": "Thank You"
        }

    return render(request, "user/home.html", context)

def index(request):
    context = {}
    if request.user.is_authenticated():
        username = request.user.get_username()
        context = {
            "user": username
        }

    return render(request, "index.html", context)


def contact(request):
    form = ContactForm(request.POST or None)

    context = {
        "form": form,

    }

    if form.is_valid():
        email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')
        from_email = 'piyushmaurya23@gmail.com'
        to_email = email
        subject = 'Email Contact Form'
        send_mail(subject, message, from_email, to_email, fail_silently=False)

    return render(request, "user/form.html", context)
