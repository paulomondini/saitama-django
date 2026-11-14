# Versão C: views com as classes genéricas do Django
# (ListView, DetailView, CreateView, UpdateView e DeleteView).
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    # template padrão: blog/post_list.html; variável: post_list


class PostDetailView(DetailView):
    # DetailView já responde com 404 se o post não existir.
    model = Post
    # template padrão: blog/post_detail.html; variável: post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # template padrão: blog/post_form.html
    # após salvar, redireciona para post.get_absolute_url()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # GET mostra blog/post_confirm_delete.html; POST apaga e redireciona.
    success_url = reverse_lazy('blog:post-list')
