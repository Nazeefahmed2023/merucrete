from django.contrib import admin
from .models import Slide, Contact, ProductCollection, ProductCard, ProductCatalogue, CatalogueCard, ProductEnquiry

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'shape_class')
    search_fields = ('title', 'subtitle')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

class ProductCardInline(admin.TabularInline):
    model = ProductCard
    extra = 1

@admin.register(ProductCollection)
class ProductCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    inlines = [ProductCardInline]

class CatalogueCardInline(admin.TabularInline):
    model = CatalogueCard
    extra = 1

@admin.register(ProductCatalogue)
class ProductCatalogueAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CatalogueCardInline]

@admin.register(ProductEnquiry)
class ProductEnquiryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'state', 'mobile')
