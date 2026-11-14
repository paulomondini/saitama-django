# Versão A: views funcionais, sem Django forms e sem validação de dados.
# Os valores são lidos diretamente de request.POST.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

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
        post = Post(
            title=request.POST['title'],
            content=request.POST['content'],
        )
        post.save()
        return redirect('blog:post-detail', pk=post.pk)
    return render(request, 'blog/post_form.html')


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('blog:post-detail', pk=post.pk)
    return render(request, 'blog/post_form.html', {'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post-list')
    # GET: mostra a página de confirmação antes de apagar.
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
