from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    """Formulário gerado a partir do modelo Post; valida os campos sozinho."""

    class Meta:
        model = Post
        fields = ['title', 'content']
        help_texts = {
            'content': 'Aceita HTML: parágrafos, títulos, listas, links e imagens.',
        }


class CommentForm(forms.ModelForm):
    """Só o texto é preenchido pelo usuário; post e autor vêm da view."""

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'short'}),
        }
        labels = {'text': 'Seu comentário'}
