from django.shortcuts import render
from django.urls import reverse_lazy
from .models import PlantingProgram
from .forms import AddPlantingProgram, UpdatePlantingProgram
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
	