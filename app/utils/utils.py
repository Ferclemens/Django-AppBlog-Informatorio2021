import logging
from functools import wraps
import time
from PIL import Image, ImageDraw, ImageFont
import random

def temporizar(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        tiempo_comienzo = time.perf_counter()
        valor = func(*args, **kwargs)
        tiempo_final = time.perf_counter()      
        tiempo_total = tiempo_final - tiempo_comienzo    
        logging.info(f"Función {func.__name__!r} corrió en {tiempo_total:.4f} segundos.")
        return valor
    return wrapper_timer

@temporizar
def paginar(obj: list, paginas_a_mostrar = 3, cuenta_posts = 0, pagina_elegida = 1, debug=False):
    
    '''Determinar la lista de páginas a mostrar según la cantidad de posts.
       Toma: Obj; Una lista que contiene todos los posts.
       Devuelve: Tupla; El primer elemento es la lista de los números entre 1 y la longitud de OBJ,
       el segundo elemento es una lista abreviada que contiene los 3 primeros números, y el número final.
       
       Keyword Arguments:
       paginas_a_mostrar: Default 3. Determina la cantidad de páginas a mostrar antes de colapsar la lista y agregar "...".
       cuenta_posts: Default 0. Indica la cantidad de posts totales. Solamente útil a modo de información
       pagina_elegida: Default 1. Indica la página que solicitamos (page/n).  
       debug: Default False. Loggea información el la consola con el nivel de prioridad INFO'''

    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
    if not debug:
        logging.disable()

    logging.info("\nLlamada función paginar.")
    logging.info(f"Lista recibida: {obj}")
    logging.info(f"kwarg Páginas a mostrar: {paginas_a_mostrar}") 
    logging.info(f"kwarg Posts totales: {cuenta_posts}")       
    
    try:
        paginas = [x+1 for x in range(obj//4)]\
                if obj % 2 == 0\
                else [x+1 for x in range((obj//4)+1)]    

        if pagina_elegida > 1:
            paginas_ab = [*paginas[pagina_elegida-2:pagina_elegida+1]]
        else:
            paginas_ab = [*paginas[:pagina_elegida+2]]

        if paginas_ab[0] - 1 > 1:
            paginas_ab = [1,
                        "...",
                        *paginas_ab]

        elif paginas_ab[0] - 1 == 1:
            paginas_ab = [1, *paginas_ab]

        if paginas[-1] - paginas_ab[-1] > 1:
            paginas_ab = [*paginas_ab,
                        "...",
                        paginas[-1]]
        elif paginas[-1] - paginas_ab[-1] == 1:
            paginas_ab = [1, *paginas_ab[1:], paginas[-1]]

        logging.info(f"Var 'paginas_ab': {paginas_ab}\n")    
    
    except IndexError:
        return [], []
        
    return (paginas, paginas_ab)


# def generar_imagenes():
#     '''
#     Genera todas las imágenes de perfil, muy interesante como para no incluírla
#     '''
#     colors = [
#         "#aa47bc",
#         "#7a1fa2",
#         "#78909c",
#         "#455964",
#         "#ec407a",
#         "#c2175b",
#         "#5c6bc0",
#         "#0288d1",
#         "#00579c",
#         "#0098a6",
#         "#00887a",
#         "#004c3f",
#         "#689f39",
#         "#ef6c00",
#         "#f5511e",
#         "#bf360c"]
    
#     letras = "ABDCEFGHIJKLMNÑOPQRSTUVWXYZ"
#     numeros = [0,1,2,3,4,5,6,7,8,9]
#     simbolos = "@/./+/-/_"
    
#     W, H = (80,80)
#     fnt = ImageFont.truetype('app/utils/fonts/Yantramanav-Light.ttf', 50)
    
#     for letra in simbolos:
#         for num in range(2):            
#             img = Image.new('RGB', (W, H), color = random.choice(colors))
#             d = ImageDraw.Draw(img)
#             msg = str(letra)
#             w, h = d.textsize(msg, font=fnt)
#             d.text(((W-w)/2,((H-h)/2)-5), msg, fill="#fdfdfe", font=fnt)

#             img.save(f'BlogInfoBase/media/users/{letra}_{num}.png')

# if __name__ == "__main__":
#     generar_imagenes()