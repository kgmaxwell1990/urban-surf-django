from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))