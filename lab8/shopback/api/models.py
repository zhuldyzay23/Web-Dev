from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name = "products", on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.name}"
