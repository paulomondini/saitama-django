from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/novo/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/editar/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/remover/', views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/comentar/', views.CommentCreateView.as_view(), name='comment-create'),
]
