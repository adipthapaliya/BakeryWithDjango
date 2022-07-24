

from django.test import Client, SimpleTestCase, TestCase
from userAccount.views import home_page
from django.contrib.auth.models import User
from django.urls import reverse, resolve

# Create your tests here.
class TestViews(TestCase):

    def test_login1(self):

        #create new user with username and password
        user = User.objects.create(username='test12')
        user.set_password('1234')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test12", password="12345")
        response = client.get(reverse(home_page))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "user/index.html")

    def test_login2(self):

        #create new user with username and password
        user = User.objects.create(username='test12')
        user.set_password('1234')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test12", password="1234")
        response = client.get(reverse(home_page))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "user/contact.html")

    def test_login3(self):

        #create new user with username and password
        user = User.objects.create(username='test12')
        user.set_password('1234')
        user.save()

        # To login 
        client = Client()
        logged_in = client.login(username="test12", password="1234")
        response = client.get(reverse(home_page))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "user/index.html")