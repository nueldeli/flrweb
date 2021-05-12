from django.urls import path 
from .views import seedling_overview, SeedlingIndexView, SeedlingDetailView, SeedlingAddView, SeedlingUpdateView, SeedlingDeleteView

urlpatterns = [
	path('', seedling_overview, name='seedling_overview'),
	path('seedling_index/', SeedlingIndexView.as_view(), name='seedling_index'),
	path('seedling_detail/<int:pk>/', SeedlingDetailView.as_view(), name='seedling_detail'),
	path('seedling_add/', SeedlingAddView.as_view(), name='seedling_add'),
	path('seedling_update/<int:pk>/', SeedlingUpdateView.as_view(), name='seedling_update'),
	path('seedling_delete/<int:pk>/', SeedlingDeleteView.as_view(), name='seedling_delete') 
]