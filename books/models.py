from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model

# from accounts.models import CustomUser


class Book(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = RichTextUploadingField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

        # return f'{self.title} از {self.author}'

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])  # /book/1


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    recommended = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.text
