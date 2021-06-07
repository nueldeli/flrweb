# Added views.py file
from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from planting.models import PlantingProgram

#def home(request):
	#return render(request, 'home.html')

def search(request):
	if request.method == 'POST':
		searched = request.POST.get('searched')
		posts = Post.objects.filter(title__contains=searched)
		programs = PlantingProgram.objects.filter(program_name__contains=searched)
		return render(request, 'search.html', {'searched':searched, 'posts':posts, 'programs':programs})
	else:
		return render(request, 'search.html', {})

class HomeView(TemplateView):
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class OrganizationView(TemplateView):
	template_name = 'organization.html'

class WdimView(TemplateView):
	template_name = 'wdim.html'
