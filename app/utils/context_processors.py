def obtener_post_destacado(request):
    from app.post.models import Post
    
    contexto={
        "post_destacado": Post.objects.all().filter(estado = True, destacado = True)[0]
    }

    return contexto

def obtener_categorias(request):
    from app.categoria.models import Categoria

    contexto = {
        "categorias": Categoria.objects.all().filter(estado=True).order_by('nombre')
    }
    return contexto