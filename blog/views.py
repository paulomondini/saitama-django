from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)

from .forms import CommentForm, PostForm
from .models import Category, Comment, Post


# ---------- Posts ----------

class PostListView(ListView):
    model = Post
    # template padrão: blog/post_list.html; variável: post_list


class PostDetailView(DetailView):
    # DetailView já responde com 404 se o post não existir.
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.object.categories.all()
        # Comentários do post, do mais recente para o mais antigo.
        context['comments'] = (
            self.object.comments.select_related('author').order_by('-posted_at')
        )
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post-list')


# ---------- Comentários ----------

class CommentCreateView(LoginRequiredMixin, CreateView):
    """Página para comentar em um post; o autor é o usuário logado."""

    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        # 404 se o post a ser comentado não existir.
        self.post_obj = get_object_or_404(Post, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context

    def form_valid(self, form):
        form.instance.post = self.post_obj
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.post_obj.get_absolute_url() + '#comentarios'


# ---------- Categorias ----------

class CategoryListView(ListView):
    model = Category
    # template padrão: blog/category_list.html; variável: category_list


class CategoryDetailView(DetailView):
    """Página de uma categoria, com todos os seus posts.

    Reaproveita o template de listagem de posts da parte 1.
    DetailView responde com 404 se a categoria não existir.
    """

    model = Category
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.object.posts.all()
        return context
