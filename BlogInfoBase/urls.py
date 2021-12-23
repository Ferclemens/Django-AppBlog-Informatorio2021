from os import name
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from app.post.views import inicio_view, registro
from django.conf.urls.static import static
from django.conf import settings
from app.usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/',views.CrearUsuarioForm.as_view(), name="registro"),
    path("", inicio_view, name="inicio"), #esta ligada a app post
    path("", include("app.post.urls", namespace="Post")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("app.categoria.urls", namespace="Cateogorias"))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
