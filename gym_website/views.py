from django.shortcuts import render, redirect
from datetime import datetime
from .models import ContactUs, FreeTrial
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = ContactUs(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Message sent successfully.')

        # Send Mail

        # send_mail('JayCee Fitness Gym & Spa', f"Thanks {name} for contacting us. We will get back to you soon!", "your_email", [email])
        # fail_silently = False

    return render(request, "home.html")

def gallery(request):
    return render(request, 'gallery.html')

def free_trial(request):

    if(request.method == "POST"):
        photo = request.POST.get('photo')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        freetrial = FreeTrial(photo='media/trialPhoto/2021/03/13/'+photo, name=name, email=email, phone=phone)
        freetrial.save()
        messages.success(request, 'Your Booking is done!')

        # Send Mail

        # send_mail('JayCee Fitness Gym & Spa', f"Thanks {name} for booking.", "your_email", [email])
        # fail_silently = False

    return render(request, 'free_trial.html')

def group_basic_pricing(request):
    return render(request, 'group_basic_pricing.html')

def group_standard_pricing(request):
    return render(request, 'group_standard_pricing.html')

def group_premium_pricing(request):
    return render(request, 'group_premium_pricing.html')

def personal_basic_pricing(request):
    return render(request, 'personal_basic_pricing.html')

def personal_standard_pricing(request):
    return render(request, 'personal_standard_pricing.html')

def personal_premium_pricing(request):
    return render(request, 'personal_premium_pricing.html')

def about(request):
    return render(request, 'about.html')
