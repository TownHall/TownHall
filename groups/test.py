__author__ = 'daniel'


from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a user.
        """
        url = reverse('user-create')
        data = {'username':'chet', 'password':'chet',
                'email':'chet@chethall.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], 'chet')
        self.assertNotEqual(response.data.get('auth-token', None), None)
        # should we test if this token works somehow?

    def test_login_user(self):
        """
        Ensure we can log in as a given user.
        """
        url = reverse('user-login')
        data = {'username':'chet', 'password':'chet'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data.get('auth-token', None), None)
        # should we test if this token works somehow?

    def test_get_user_details(self):
        """
        Ensure we can get user details.
        """
        url = reverse('user-details')
        data = {'username':'chet'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('username', None), 'chet')
        self.assertEqual(response.data.get('groups', None), ['SECSI'])

class GroupTests(APITestCase):
    def setUp(self):
        user = User.objects.create_user('chad', 'chad@chadhall.com', 'chad')

    def test_create_group(self):
        """
        Ensure we can create a group.
        """
        url = reverse('group-create')
        user = User.objects.get(username='chad')
        token = Token.objects.get_or_create(user=user)
        data = {'auth-token': token, 'name':'SECSI',
                'description':'SECSI, DO YOU SPEAK IT'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
