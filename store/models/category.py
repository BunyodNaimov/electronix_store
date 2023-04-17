from django.db import models
from .store import Category

class Electronic(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    sale_percent = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    pub_year = models.PositiveIntegerField(null=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title