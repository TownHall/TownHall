# -*- coding: utf-8 -*-
__author__ = 'daniel'


from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from provider.oauth2.models import Client, AccessToken
import datetime

class UserTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """
        Ensure we can create a user.
        """
        url = reverse('user-create')
        data = {'username': 'chet', 'password': 'chet',
                'email':'chet@chethall.com', 'format':'json'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data.get('access_token', None), None)

    def test_login_user(self):
        """
        Ensure we can log in as a given user.
        """
        user = User.objects.create_user(username='chet', email='chet@chethall.com', password='chet')
        cl =  Client.objects.create(user=user,
                                    redirect_uri="http://localhost/",
                                    client_type=2
        )

        token = AccessToken.objects.create(user=user, client=cl,
                            expires=datetime.date(year=2015,month=1,day=2)
        )
        url = reverse('user-login')
        data = {'username': 'chet',
                'password': 'chet', 'format': 'json'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data.get('access_token', None), None)

        # I'm testing that the login worked by following up and creating a group.
        # This is sort of an unwieldy test, but I'm not sure what a better way to
        # do it is.
        url = reverse('group-create')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data["access_token"]
        )

        data = {
                'creator': user.id, 'name': 'SECSI', 'description': 'SECSI DO YOU SPEAK IT?',
                }
        response2 = self.client.post(url + ".json", data, format='json')
        self.assertEqual(response2.data["name"], "SECSI")

    def test_get_user_details(self):
        """
        Ensure we can get user details.
        """
        user = User.objects.create_user(username='chort', email='chort@chorthall.com', password='chort')
        url = reverse('user-details', args=(user.id,))
        response = self.client.get(url + ".json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'chort')


class GroupTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='chet', email='chet@chethall.com', password='chet')
        self.cl =  Client.objects.create(user=self.user,
                                         redirect_uri="http://localhost/",
                                         client_type=2
        )

        self.token = AccessToken.objects.create(
            user=self.user, client=self.cl,
            expires=datetime.date(
                year=2015, month=1, day=2
            )
        )
        self.client = APIClient()

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.token)


    def test_create_group(self):
        """
        Ensure we can create a group.
        """
        url = reverse('group-create')
        data = { 'name': 'SECSI',
                'description': 'SECSI, DO YOU SPEAK IT', 'creator': self.user.id}
        response = self.client.post(url + ".json", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)