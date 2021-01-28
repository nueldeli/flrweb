from django.urls import path
from .views import PostView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
	path('', PostView.as_view(), name='post_index'),
	path('post_add', AddPostView.as_view(), name='post_add'),
	path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),
	path('post_update/<int:pk>', UpdatePostView.as_view(), name='post_update'),
	path('post_delete/<int:pk>', DeletePostView.as_view(), name='post_delete')
]