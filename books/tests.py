from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime

from .models import Book


def date(year, month, day):
    return datetime.date(year, month, day)


class BookStoreTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book1 = Book.objects.create(
            title='اثر مرکب',
            author='دارن هاردی',
            description='A variation on the question technique above, the multiple-choice question great way to engage your reader',
            price='22.99',
            cover='media/avatars/test.jpg',
            status=Book.STATUS_CHOICES[0][0],  # Published
        )
        cls.book2 = Book.objects.create(
            title='اثر مرکب 2',
            author='دارن هاردی 2',
            description='A variation on the question technique above, the multiple-choice question great way to engage your reader 22',
            price='24.99',
            cover='media/avatars/test.jpg',
            status=Book.STATUS_CHOICES[1][0],  # Draft
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book2.title)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.author)
        self.assertContains(response, self.book1.description)
        self.assertContains(response, self.book1.price)
        self.assertContains(response, self.book1.cover)
        self.assertTemplateUsed(response, 'books/book_detail.html')

    def test_book_create_view(self):
        response = self.client.get(reverse('book_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_create.html')

    def test_book_create_form(self):
        response = self.client.post(reverse('book_create'), {
            'title': 'اثر مرکب',
            'author': 'دارن هاردی',
            'description': 'A variation on the question technique above, the multiple-choice question great way to engage your reader',
            'price': '22.99',
            'cover': 'media/avatars/test.jpg',
            'status': Book.STATUS_CHOICES[0][0],  # Published
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 3)

    def test_book_update_view(self):
        response = self.client.get(reverse('book_update', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_update.html')

    def test_book_update_form(self):
        response = self.client.post(reverse('book_update', args=[self.book1.id]), {
            'title': 'اثر مرکب',
            'author': 'دارن هاردی',
            'description': 'A variation on the question technique above, the multiple-choice question great way to engage your reader',
            'price': '22.99',
            'cover': 'media/avatars/test.jpg',
            'status': Book.STATUS_CHOICES[0][0],  # Published
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 2)

    def test_book_delete_view(self):
        response = self.client.get(reverse('book_delete', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_delete.html')

    def test_book_delete_form(self):
        response = self.client.post(reverse('book_delete', args=[self.book1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 1)


