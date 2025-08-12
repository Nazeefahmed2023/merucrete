from django.shortcuts import render
from .models import Slide, Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    slides = Slide.objects.all()
    return render(request, 'index.html', {'slides': slides})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        # Save to DB
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        # Email logic (based on your ref)
        subject = "New Contact Form Submission"
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message:
        {message}
        """
        send_mail(subject, body, settings.EMAIL_HOST_USER, ['mohammedsowban008@gmail.com'], fail_silently=False)

        messages.success(request, "Thank you for contacting us!")

    return render(request, 'contactus.html')

def product_view(request):
    return render(request, 'product.html')

def about_view(request):
    return render(request, 'about.html')


from django.shortcuts import render
from .models import ProductCollection

def product_section(request):
    series = ProductCollection.objects.prefetch_related('cards').all()
    return render(request, 'product.html', {'series': series})

from django.shortcuts import render
from .models import ProductCatalogue

def product_catalogue_view(request):
    series = ProductCatalogue.objects.all()
    return render(request, 'product2.html', {'series': series})

# shop/views.py
from django.shortcuts import redirect
from django.contrib import messages
from .models import ProductEnquiry

def save_enquiry(request):
    if request.method == 'POST':
        product_name = request.POST.get('productName')
        address = request.POST.get('address')
        state = request.POST.get('state')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        ProductEnquiry.objects.create(
            product_name=product_name,
            address=address,
            state=state,
            mobile=mobile,
            message=message
        )
        messages.success(request, "Your enquiry has been submitted successfully!")

    return redirect('product')  # or whatever page you want to redirect after form submit


from django.shortcuts import redirect
from django.contrib import messages
from .models import ProductEnquiry

def save_enquiry(request):
    if request.method == 'POST':
        product_name = request.POST.get('productName')
        address = request.POST.get('address')
        state = request.POST.get('state')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        ProductEnquiry.objects.create(
            product_name=product_name,
            address=address,
            state=state,
            mobile=mobile,
            message=message
        )
        messages.success(request, "Your enquiry has been submitted successfully!")
        return redirect('product_section')  # Redirect to the product page or any URL name

    return redirect('product_section')
