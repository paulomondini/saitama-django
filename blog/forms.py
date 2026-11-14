from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """Formulário gerado a partir do modelo Post; valida os campos sozinho."""

    class Meta:
        model = Post
        fields = ['title', 'content']
        help_texts = {
            'content': 'Aceita HTML: parágrafos, títulos, listas, links e imagens.',
        }
