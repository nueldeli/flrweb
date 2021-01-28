from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SubscribeForm
from .models import Subs

# Create your views here.
class SubscribeView(CreateView):
	model = Subs
	form_class = SubscribeForm
	template_name = 'subscription/subscription.html'