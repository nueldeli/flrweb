# Added views.py file
from django.shortcuts import render
from subscription.forms import SubscribeForm

def home(request):
	return render(request, 'home.html')