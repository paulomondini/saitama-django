from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # Páginas prontas de login/logout do próprio Django.
    path('conta/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
]

if not settings.DEBUG:
    # Em produção (Render), serve o CSS do admin usando apenas o Django,
    # sem bibliotecas extras.
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT}),
    ]
