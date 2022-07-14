from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Book(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    cover = models.ImageField(upload_to='media/covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', args=[self.id])  # /book/1
