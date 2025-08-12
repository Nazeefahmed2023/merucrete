from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact_us'),
    path('about/', views.about_view, name='about'),
    path('product-catalogue/', views.product_catalogue_view, name='product_catalogue'),
    path('products/', views.product_section, name='product_section'),
    path('submit-enquiry/', views.save_enquiry, name='save_enquiry'),
]

# This serves media & static files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
