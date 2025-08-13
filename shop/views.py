from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Slide, Contact, ProductCollection, ProductCatalogue, ProductEnquiry

def index(request):
    slides = Slide.objects.all()
    return render(request, 'index.html', {'slides': slides})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        Contact.objects.create(name=name, email=email, phone=phone, message=message)

        send_mail(
            "New Contact Form Submission",
            f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}",
            settings.EMAIL_HOST_USER,
            ['mohammedsowban008@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Thank you for contacting us!")

    return render(request, 'contactus.html')

def about_view(request):
    return render(request, 'about.html')

def product_section(request):
    series = ProductCollection.objects.prefetch_related('cards').all()
    return render(request, 'product.html', {'series': series})

def product_catalogue_view(request):
    series = ProductCatalogue.objects.all()
    return render(request, 'product2.html', {'series': series})

def save_enquiry(request):
    if request.method == 'POST':
        ProductEnquiry.objects.create(
            product_name=request.POST.get('productName'),
            address=request.POST.get('address'),
            state=request.POST.get('state'),
            mobile=request.POST.get('mobile'),
            message=request.POST.get('message')
        )
        messages.success(request, "Your enquiry has been submitted successfully!")
    return redirect('product_section')
