from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('email',)
    ordering = ('-id',)


from django.contrib import admin
from .models import Slide

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'shape_class')  # What to display in the list view
    search_fields = ('title', 'subtitle')  # Fields to search by
    list_filter = ('shape_class',)  # Add filter by shape class in the admin panel
    
    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'background_image', 'shape1', 'shape2', 'shape3', 'shape_class')
        }),
    )

from django.contrib import admin
from .models import ProductCollection, ProductCard

class ProductCardInline(admin.TabularInline):
    model = ProductCard
    extra = 1

@admin.register(ProductCollection)
class ProductCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    inlines = [ProductCardInline]


from django.contrib import admin
from .models import ProductCatalogue, CatalogueCard

class CatalogueCardInline(admin.TabularInline):
    model = CatalogueCard
    extra = 1

class ProductCatalogueAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CatalogueCardInline]

admin.site.register(ProductCatalogue, ProductCatalogueAdmin)

from django.contrib import admin
from .models import ProductEnquiry

admin.site.register(ProductEnquiry)
