# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class Slide(models.Model):
    SHAPE_CLASS_CHOICES = [
        ('shape-tri', 'Triangle'),
        ('shape-circ', 'Circle'),
        ('shape-boxy', 'Box'),
    ]

    title = models.CharField(max_length=200, default="Transform Your Space with Elegance!")
    subtitle = models.CharField(max_length=300, default="Premium Cultured Stones for Interior & Exterior Excellence")
    background_image = models.ImageField(upload_to='slider/backgrounds/', default='slider/backgrounds/default1.jpg')
    shape1 = models.ImageField(upload_to='slider/shapes/', default='slider/shapes/triangle1.avif')
    shape2 = models.ImageField(upload_to='slider/shapes/', default='slider/shapes/triangle2.jpg')
    shape3 = models.ImageField(upload_to='slider/shapes/', default='slider/shapes/triangle3.jpg')

    shape_class = models.CharField(
        max_length=50,
        choices=SHAPE_CLASS_CHOICES,
        default='shape-tri',
        help_text="Select a shape style: Triangle / Circle / Box"
    )

    def __str__(self):
        return self.title


from django.db import models

class ProductCollection(models.Model):
    title = models.CharField(max_length=100, help_text="E.g. VIANA LEDGE")
    subtitle = models.CharField(max_length=100, help_text="E.g. SERIES")
    main_image = models.ImageField(upload_to='products/main/')
  

    def __str__(self):
        return f"{self.title} {self.subtitle}"

class ProductCard(models.Model):
    collection = models.ForeignKey(ProductCollection, related_name='cards', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/cards/')
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.color} ({self.size})"


from django.db import models

class ProductCatalogue(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='product_catalogue_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class CatalogueCard(models.Model):
    product = models.ForeignKey(ProductCatalogue, related_name='cards', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='catalogue_card_images/')
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.color} - {self.size}"

class ProductEnquiry(models.Model):
    product_name = models.CharField(max_length=200)
    address = models.TextField()
    state = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry for {self.product_name} from {self.mobile}"
