from django.test import TestCase, SimpleTestCase

from django.contrib.auth import get_user_model

from django.urls import reverse

# Create your tests here.


class HomePageTests(SimpleTestCase):

    # test if home page exists

    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    # test if home page is resolved by name

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # test if home page is using coreect template

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

    # insert testing values for test

    username = 'newuser'
    email = 'newuseregmail.com'

    # test if signup page exists

    def test_signup_page_status_code(self):
        response = self.client.get('/user/signup/')
        self.assertEqual(response.status_code, 200)

    # test if signup page is resolved by name

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    # test if signup page is using correct template

    def test_view_usage_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    # test if signup page taking correct values

    def test_signup_form(self):

        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)



