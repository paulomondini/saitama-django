from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('posts/novo/', views.post_create, name='post-create'),
    path('posts/<int:pk>/editar/', views.post_update, name='post-update'),
    path('posts/<int:pk>/remover/', views.post_delete, name='post-delete'),
]
