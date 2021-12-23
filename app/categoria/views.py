from django.shortcuts import render
from app.post.models import Post
from django.core.paginator import Paginator
from app.utils.utils import paginar, temporizar
from django.http.response import HttpResponseRedirect


@temporizar
def vista_categoria(request, *args, **kwargs):
    posts = Post.objects.filter(categoria__nombre=kwargs["cat"], estado=True)   
    
    if 'num' in kwargs:
        posts_a_mostrar = posts[(kwargs["num"]-1)*4:]
    else:
        posts_a_mostrar = posts

    p = Paginator(posts_a_mostrar, 2)
       
    posts_paginados = [p.page(x+1).object_list for x in range(p.num_pages)]

    
    if 'busqueda' in request.GET and request.GET['busqueda'] != "":
        return HttpResponseRedirect(f"/search/{request.GET['busqueda']}")
    
    contexto = {
        "posts": posts,                        
        "paginas": posts_paginados,        
        "numero_paginas": paginar(len(posts))[1],
        "categoria": kwargs["cat"]   
        }

    if 'num' in kwargs:
        contexto["numero_paginas"] = paginar(len(posts), cuenta_posts=len(posts), pagina_elegida= kwargs["num"])[1]
        contexto["posts_a_mostrar"] = posts[(kwargs["num"]-1)*4:]
        
    return render(request, "categoria/categoria.html", context=contexto)