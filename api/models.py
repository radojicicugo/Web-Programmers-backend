from django.db import models

# Create your models here.
class Api(models.Model):
    image = models.ImageField(upload_to='uploads/images', null=False, blank=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    email = models.EmailField(auto_created=True, blank=False)
    description = models.TextField()
    new_category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name