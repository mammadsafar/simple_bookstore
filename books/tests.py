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

    # def test_signup_page_status_code(self):
    #     response = self.client.get('/accounts/signup/')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_view_url_by_name(self):
    #     response = self.client.get(reverse('signup'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('signup'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'registration/signup.html')
    #
    # def test_signup_page_template_used(self):
    #     response = self.client.get(reverse('signup'))
    #     self.assertTemplateUsed(response, 'registration/signup.html')
    #
    # def test_signup_page_form(self):
    #     user = get_user_model().objects.create_user(
    #         username=self.username,
    #         email=self.email,
    #         password=self.password,
    #         first_name=self.first_name,
    #         last_name=self.last_name,
    #         phone_number=self.phone_number,
    #         date_of_birth=self.date_of_birth,
    #         avatar=self.avatar
    #     )
    #     self.assertEqual(get_user_model().objects.all().count(), 1)
    #     self.assertEqual(get_user_model().objects.all()[0].username, self.username)
    #     self.assertEqual(get_user_model().objects.all()[0].email, self.email)
    #     self.assertEqual(get_user_model().objects.all()[0].check_password(self.password), True)
    #     self.assertEqual(get_user_model().objects.all()[0].first_name, self.first_name)
    #     self.assertEqual(get_user_model().objects.all()[0].last_name, self.last_name)
    #     self.assertEqual(get_user_model().objects.all()[0].phone_number, self.phone_number)
    #     self.assertEqual(get_user_model().objects.all()[0].date_of_birth, self.date_of_birth)
    #     self.assertEqual(get_user_model().objects.all()[0].avatar, self.avatar)
