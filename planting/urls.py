from django.urls import path
from .views import PlantingHome, PlantingProgramIndex, PlantingProgramDetail, PlantingProgramAdd, PlantingProgramUpdate, PlantingProgramDelete

urlpatterns = [
	path('', PlantingHome.as_view(), name='planting_home'),
	path('planting_program_index/', PlantingProgramIndex.as_view(), name='planting_program_index'),
	path('planting_program_detail/<int:pk>/', PlantingProgramDetail.as_view(), name='planting_program_detail'),
	path('planting_program_add/', PlantingProgramAdd.as_view(), name='planting_program_add'),
	path('planting_program_update/<int:pk>/', PlantingProgramUpdate.as_view(), name='planting_program_update'),
	path('planting_program_delete/<int:pk>/', PlantingProgramDelete.as_view(), name='planting_program_delete'),
]