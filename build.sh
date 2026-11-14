#!/usr/bin/env bash
# Roteiro executado pelo Render a cada publicação (deploy).
set -o errexit

pip install -r requirements.txt

# Copia os arquivos estáticos (CSS do admin) para a pasta staticfiles/.
python manage.py collectstatic --no-input

# Cria as tabelas no banco SQLite e carrega o conteúdo da wiki.
python manage.py migrate
python manage.py loaddata wiki

# Cria o superusuário a partir das variáveis de ambiente configuradas no Render.
if [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  python manage.py createsuperuser --no-input || true
fi
