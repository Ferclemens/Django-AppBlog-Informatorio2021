from os import name
from django.urls import path
from . import views

app_name = "post"
urlpatterns = [       
    path('post/<slug:post>/', views.vista_post, name="vista_post"),
    path('page/<int:num>', views.vista_paginada, name="vista_paginada"),
    path('search/<str:query>', views.vista_busqueda, name="vista_busqueda"),
    path('search/<str:query>/page<int:num>', views.vista_busqueda, name="vista_busqueda_paginada"),
    path('fecha/<str:fecha>', views.vista_fecha, name="vista_fecha"),
    path('fecha/<str:fecha>/<int:num>', views.vista_fecha, name="vista_fecha_paginada"),
    path('visitas/', views.vista_visitas, name="vista_visitas"),
    path('visitas/<int:num>', views.vista_visitas, name="vista_visitas_paginada"),
    path('comentarios/', views.vista_comentarios, name="vista_comentarios"),
    path('comentarios/<int:num>', views.vista_comentarios, name="vista_comentarios_paginada")
] 