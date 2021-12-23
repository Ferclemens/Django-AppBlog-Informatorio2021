from django.urls import path
from . import views


app_name = "categoria"
urlpatterns = [
    path('categoria/<str:cat>/', views.vista_categoria, name="vista_categoria"),
    path('categoria/<str:cat>/page/<int:num>', views.vista_categoria, name="vista_categoria_paginada")
]