from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import datetime


def date(year, month, day):
    return datetime.date(year, month, day)


class SignUpPageTest(TestCase):
    username = 'test'
    email = 'test@test.com'
    password = 'test'
    first_name = 'first_test'
    last_name = 'last_test'
    phone_number = '123456789'
    date_of_birth = date(2000, 1, 1)
    avatar = 'media/avatars/test.jpg'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_page_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_page_form(self):
        user = get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            phone_number=self.phone_number,
            date_of_birth=self.date_of_birth,
            avatar=self.avatar
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        self.assertEqual(get_user_model().objects.all()[0].check_password(self.password), True)
        self.assertEqual(get_user_model().objects.all()[0].first_name, self.first_name)
        self.assertEqual(get_user_model().objects.all()[0].last_name, self.last_name)
        self.assertEqual(get_user_model().objects.all()[0].phone_number, self.phone_number)
        self.assertEqual(get_user_model().objects.all()[0].date_of_birth, self.date_of_birth)
        self.assertEqual(get_user_model().objects.all()[0].avatar, self.avatar)
