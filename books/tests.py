from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, )
from django.views.generic import View
from accounts.models import CustomUser
from .models import Book


def date(year, month, day):
    return datetime.date(year, month, day)


#
# class EmptyResponseView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse()
#
#
# class StackedMixinsView1(LoginRequiredMixin, PermissionRequiredMixin, EmptyResponseView):
#     permission_required = ['auth_tests.add_customuser', 'auth_tests.change_customuser']
#     raise_exception = True


class BookStoreTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(
            username="Test",
            password="Test",
            email="test@test.com",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            last_login=datetime.datetime.now(),
            date_joined=datetime.datetime.now(),
            first_name="Test",
            last_name="Test",
            phone_number="123456789",
            date_of_birth=date(1990, 1, 1),
            avatar="avatars/test.jpg",
        )
        # login with superuser
        cls.book1 = Book.objects.create(
            user=cls.user,
            title='اثر مرکب',
            author='دارن هاردی',
            description='A variation on the question technique above, the multiple-choice question great way to engage your reader',
            price='22.99',
            cover='media/avatars/test.jpg',
            status=Book.STATUS_CHOICES[0][0],  # Published
        )
        cls.book2 = Book.objects.create(
            user=cls.user,
            title='اثر مرکب 2',
            author='دارن هاردی 2',
            description='A variation on the question technique above, the multiple-choice question great way to engage your reader 22',
            price='24.99',
            cover='media/avatars/test.jpg',
            status=Book.STATUS_CHOICES[1][0],  # Draft
        )

    #     cls.client = Client()
    #     # cls.client.login(username="Test", password="Test")
    #     cls.client.post('/login/', {'name': 'Test', 'passwd': 'Test'})
    #     print('---------- login with superuser ----------')
    #     print(cls.user.is_authenticated)
    #
    # def test_login_user(self):
    #
    #     print('---------- login with superuser ----------')
    #     print(self.user.is_authenticated)
    #     response = self.client.get(reverse('book_create'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '/accounts/login/?next=/books/create/')

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
        self.client.login(username="Test", password="Test")
        response = self.client.get(reverse('book_create'))
        print('---------- login with superuser ----------')
        print(response.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_create.html')

    def test_book_create_form(self):
        self.client.login(username="Test", password="Test")
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
