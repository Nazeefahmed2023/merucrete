from django.db import models
from .utils import upload_file_and_get_public_url

# ----- Slides -----
class Slide(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    background_image = models.ImageField(upload_to='slides/', blank=True, null=True)
    background_image_url = models.URLField(max_length=500, blank=True, null=True)

    shape1 = models.ImageField(upload_to='slides/', blank=True, null=True)
    shape1_url = models.URLField(max_length=500, blank=True, null=True)

    shape2 = models.ImageField(upload_to='slides/', blank=True, null=True)
    shape2_url = models.URLField(max_length=500, blank=True, null=True)

    shape3 = models.ImageField(upload_to='slides/', blank=True, null=True)
    shape3_url = models.URLField(max_length=500, blank=True, null=True)

    shape_class = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.background_image:
            self.background_image_url = upload_file_and_get_public_url(
                self.background_image, f"slides/{self.background_image.name}"
            )
        if self.shape1:
            self.shape1_url = upload_file_and_get_public_url(
                self.shape1, f"slides/{self.shape1.name}"
            )
        if self.shape2:
            self.shape2_url = upload_file_and_get_public_url(
                self.shape2, f"slides/{self.shape2.name}"
            )
        if self.shape3:
            self.shape3_url = upload_file_and_get_public_url(
                self.shape3, f"slides/{self.shape3.name}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ----- Contact -----
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name


# ----- Products -----
class ProductCollection(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class ProductCard(models.Model):
    collection = models.ForeignKey(
        ProductCollection, related_name='cards', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, default="Unnamed Product")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
      # Always numeric default

    def save(self, *args, **kwargs):
        if self.image:
            self.image_url = upload_file_and_get_public_url(
                self.image, f"products/{self.image.name}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


# ----- Product Catalogue -----
class ProductCatalogue(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CatalogueCard(models.Model):
    catalogue = models.ForeignKey(
        ProductCatalogue, related_name='cards', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255, default="Untitled Catalogue Item")
    image = models.ImageField(upload_to='catalogues/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.image_url = upload_file_and_get_public_url(
                self.image, f"catalogues/{self.image.name}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ----- Enquiries -----
class ProductEnquiry(models.Model):
    product_name = models.CharField(max_length=255)
    address = models.TextField()
    state = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Enquiry for {self.product_name}"
