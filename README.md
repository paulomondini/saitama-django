# Saitama Wiki

Fórum/wiki de fãs de **One-Punch Man** feito com Django, como segunda entrega
de laboratório (aplicação CRUD).

## Funcionalidades

- **Posts (artigos):** listagem, página individual, criação, edição e remoção
  com página de confirmação. O conteúdo é guardado em HTML.
- **Comentários:** exibidos na página do post (mais recentes primeiro);
  membros logados podem comentar.
- **Categorias:** cada post pode ter várias; há uma página com todas as
  categorias e uma página por categoria listando seus posts.
- **Admin do Django** com os modelos `Post`, `Comment` e `Category`.

Criar, editar, remover e comentar exige login. As contas são criadas pelo
superusuário no admin (`/admin/`).

## Histórico (Git)

| Commit / branch | Conteúdo |
|---|---|
| versão A | views funcionais sem Django forms e sem validação |
| versão B | views funcionais com `PostForm` (Django form) |
| versão C | views com `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` |
| branch `comments` | modelo `Comment` e view de criação de comentários |
| branch `categories` | modelo `Category` e views de categorias |

## Rodar localmente

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows (no Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata wiki     # conteúdo de exemplo
python manage.py createsuperuser
python manage.py runserver
```

Depois, abra http://127.0.0.1:8000/.

## Deploy no Render

O arquivo `render.yaml` descreve o serviço, e o `build.sh` instala as
dependências, cria o banco e carrega o conteúdo de `blog/fixtures/wiki.json`.
No plano gratuito o disco não é permanente: a cada nova publicação o banco é
recriado a partir desse arquivo.
