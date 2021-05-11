from django.urls import path 
from .views import SeedlingDataOverview, SeedlingIndexView, SeedlingDetailView, SeedlingAddView, SeedlingUpdateView, SeedlingDeleteView

urlpatterns = [
	path('', SeedlingDataOverview.as_view(), name='seedling_overview'),
	path('seedling_index/', SeedlingIndexView.as_view(), name='seedling_index'),
	path('seedling_detail/<int:pk>/', SeedlingDetailView.as_view(), name='seedling_detail'),
	path('seedling_add/', SeedlingAddView.as_view(), name='seedling_add'),
	path('seedling_update/', SeedlingUpdateView.as_view(), name='seedling_update'),
	path('seedling_delete/', SeedlingDeleteView.as_view(), name='seedling_delete') 
]