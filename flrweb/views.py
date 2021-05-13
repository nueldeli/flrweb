# Added views.py file
from django.shortcuts import render
from django.views.generic import TemplateView

#def home(request):
	#return render(request, 'home.html')

class HomeView(TemplateView):
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class OrganizationView(TemplateView):
	template_name = 'organization.html'

class WdimView(TemplateView):
	template_name = 'wdim.html'
