from django.urls import path 
from .views import seedling_overview, sabal_index, niah_index, semengoh_index, SeedlingIndexView, SeedlingDetailView, SeedlingAddView, SeedlingUpdateView, SeedlingDeleteView

urlpatterns = [
	path('', seedling_overview, name='seedling_overview'),
	path('sabal_index/', sabal_index, name='sabal_index'),
	path('niah_index/', niah_index, name='niah_index'),
	path('IFRC_index/', semengoh_index, name='semengoh_index'),
	path('seedling_index/', SeedlingIndexView.as_view(), name='seedling_index'),
	path('seedling_detail/<int:pk>/', SeedlingDetailView.as_view(), name='seedling_detail'),
	path('seedling_add/', SeedlingAddView.as_view(), name='seedling_add'),
	path('seedling_update/<int:pk>/', SeedlingUpdateView.as_view(), name='seedling_update'),
	path('seedling_delete/<int:pk>/', SeedlingDeleteView.as_view(), name='seedling_delete') 
]