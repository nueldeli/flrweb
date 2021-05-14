from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Seedling
from .forms import AddSeedlingForm, UpdateSeedlingForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Sum

data_object = Seedling.objects.all()

# Create your views here.
def seedling_overview(request):
	sabal_total_species = data_object.filter(nursery__icontains='Sabal').count()
	niah_total_species = data_object.filter(nursery__icontains='Niah').count()
	semengoh_total_species = data_object.filter(nursery__icontains='IFRC').count()
	cumulative_species = data_object.count()
	cumulative_quantity = data_object.aggregate(Sum('quantity'))['quantity__sum']
	label = ['Sabal FLR Centre', 'Niah FRS', 'IFRC Semengoh']
	data = [sabal_total_species, niah_total_species, semengoh_total_species]
	return render(request, 'dms/seedling_overview.html', {
		'sabal_total_species':sabal_total_species,
		'niah_total_species':niah_total_species,
		'semengoh_total_species':semengoh_total_species,
		'cumulative_species':cumulative_species,
		'cumulative_quantity':cumulative_quantity,
		'label':label,
		'data':data
		})

def sabal_index(request):
	sabal_nursery_index = data_object.filter(nursery__icontains='Sabal')
	return render(request, 'dms/sabal_index.html', {'sabal_nursery_index':sabal_nursery_index})

def niah_index(request):
	niah_nursery_index = data_object.filter(nursery__icontains='Niah')
	return render(request, 'dms/niah_index.html', {'niah_nursery_index':niah_nursery_index})

def semengoh_index(request):
	semengoh_nursery_index = data_object.filter(nursery__icontains='IFRC')
	return render(request, 'dms/semengoh_index.html', {'semengoh_nursery_index':semengoh_nursery_index})

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

