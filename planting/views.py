from django.shortcuts import render
from django.urls import reverse_lazy
from .models import PlantingProgram, Item
from .forms import AddPlantingProgram, UpdatePlantingProgram, AddItem, UpdateItem
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class PlantingHome(TemplateView):
	template_name = 'planting/planting_home.html'

class PlantingProgramIndex(ListView):
	model = PlantingProgram
	template_name = 'planting/planting_program_index.html'

class PlantingProgramDetail(DetailView):
	model = PlantingProgram
	template_name = 'planting/planting_program_detail.html'

class PlantingProgramAdd(CreateView):
	model = PlantingProgram
	form_class = AddPlantingProgram
	template_name = 'planting/planting_program_add.html'

class PlantingProgramUpdate(UpdateView):
	model = PlantingProgram
	form_class = UpdatePlantingProgram
	template_name = 'planting/planting_program_update.html'

class PlantingProgramDelete(DeleteView):
	model = PlantingProgram
	template_name = 'planting/planting_program_delete.html'
	success_url = reverse_lazy('planting_program_index')
	
class ItemIndex(ListView):
	model = Item
	template_name = 'planting/item_index.html'
	
class ItemAdd(CreateView):
	model = Item
	form_class = AddItem
	template_name = 'planting/item_add.html'

class ItemUpdate(UpdateView):
	model = Item
	form_class = UpdateItem
	template_name = 'planting/item_update.html'

class ItemDelete(DeleteView):
	model = Item
	template_name = 'planting/item_delete.html'
	success_url = reverse_lazy('item_index')

