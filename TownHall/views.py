__author__ = 'daniel'
from django.views.generic import View
from django.shortcuts import render, redirect
from forms import LoginForm
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class home(View):
    def get(self, request):
        # <view logic>
        form = LoginForm()
        c = { 'form' : form }
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


class UserCreate(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        user = User.objects.create_user(username, email, password)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/users/' + str(user.id))
