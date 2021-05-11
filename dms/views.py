from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Seedling
from .forms import AddSeedlingForm, UpdateSeedlingForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class SeedlingDataOverview(TemplateView):
	template_name = 'dms/seedling_overview.html'

class SeedlingIndexView(ListView):
	model = Seedling
	template_name = 'dms/seedling_index.html'

class SeedlingDetailView(DetailView):
	model = Seedling
	template_name = 'dms/seedling_detail.html'

class SeedlingAddView(CreateView):
	model = Seedling
	template_name = 'dms/seedling_add.html'
	form_class = AddSeedlingForm

class SeedlingUpdateView(UpdateView):
	model = Seedling
	template_name = 'dms/seedling_update.html'
	form_class = UpdateSeedlingForm

class SeedlingDeleteView(DeleteView):
	model = Seedling
	template_name = 'dms/seedling_delete.html'
	success_url = reverse_lazy('seedling_index')

