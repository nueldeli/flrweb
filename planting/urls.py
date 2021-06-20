from django.urls import path
from .views import PlantingHome, PlantingProgramIndex, PlantingProgramDetail, PlantingProgramAdd, PlantingProgramUpdate, PlantingProgramDelete, ItemIndex, ItemAdd, ItemUpdate, ItemDelete

urlpatterns = [
	path('', PlantingHome.as_view(), name='planting_home'),
	path('planting_program_index/', PlantingProgramIndex.as_view(), name='planting_program_index'),
	path('planting_program_detail/<int:pk>/', PlantingProgramDetail.as_view(), name='planting_program_detail'),
	path('planting_program_add/', PlantingProgramAdd.as_view(), name='planting_program_add'),
	path('planting_program_update/<int:pk>/', PlantingProgramUpdate.as_view(), name='planting_program_update'),
	path('planting_program_delete/<int:pk>/', PlantingProgramDelete.as_view(), name='planting_program_delete'),
	path('item_index/', ItemIndex.as_view(), name='item_index'),
	path('item_add/', ItemAdd.as_view(), name='item_add'),
	path('item_update/<int:pk>', ItemUpdate.as_view(), name='item_update'),
	path('item_delete/<int:pk>', ItemDelete.as_view(), name='item_delete'),
]