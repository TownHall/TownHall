# -*- coding: utf-8 -*-
__author__ = 'daniel'

from django.views.generic import View
from django.shortcuts import render, redirect
from forms import LoginForm
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from groups.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from provider.oauth2.models import Client, AccessToken
import datetime


class home(View):
    def get(self, request):
        # <view logic>
        form = LoginForm()
        c = {'form': form}
        c.update(csrf(request))
        return render(request, 'home.html', c)

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user.is_active:
            login(request, user)
            return redirect('/users/' + str(user.id))
        else:
            return self.get(request)


class UserCreate(APIView):
    def post(self, request):
        print
        "creating a goddamned user"
        print
        request.DATA
        print
        dir(request)
        username = request.DATA.get('username', '')
        password = request.DATA.get('password', '')
        email = request.DATA.get('email', '')
        print
        username
        user = User.objects.create_user(username, email, password)
        user = authenticate(username=username, password=password)
        cl = Client.objects.create(user=user, name=username,
                                   redirect_uri="http://localhost/",
                                   client_type=2
        )

        token = AccessToken.objects.create(user=user, client=cl,
                                           expires=datetime.date(year=2015, month=1, day=2)
        )
        if self.request.accepted_renderer.format == 'json':
            response = Response({'access_token': token.token})
            response.status_code = status.HTTP_201_CREATED
            return response
        login(request, user)
        return redirect('/users/' + str(user.id))
