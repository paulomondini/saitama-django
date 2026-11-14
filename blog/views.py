# Versão B: views funcionais utilizando um Django form (PostForm),
# que valida os dados antes de salvar.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post_list': posts})


def post_detail(request, pk):
    # get_object_or_404 responde com erro 404 se o post não existir.
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post-list')
    # GET: mostra a página de confirmação antes de apagar.
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
