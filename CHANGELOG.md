# Log de Cambios

En este archivo se definen en profundidad los cambios realizados en cada commit.

Al marcar los cambios, se utiliza la fecha del cambio y se sigue el estándar de [Versionado Semántico 2.0.0].  
(Solo se usa el concepto MAYOR.MENOR.PARCHE para no complicarse la vida)

Este sistema funciona de la siguiente manera:

- La versión **MAYOR** cuando realizas un cambio incompatible con el resto del proyecto. (Ejemplo: Se cambia o agrega un modelo)
- La versión **MENOR** cuando añades funcionalidad que es compatible con versiones anteriores. (Ejemplo: Se modifica un .html o .css)
- La versión **PARCHE** cuando reparas errores compatibles con versiones anteriores. (Ejemplo: Se soluciona un bug/error pequeño)

---

## Vesión (0.1.0) (04/12/21)

### Cambios

### app/post/models.py

- Añadida función `user_directory_path`: Devuelve un string con la dirección donde se debe guardar la imagen de cada post.
- Cambio de atributo `img`; de `URLField` a `ImageField`.

### app/categoria/models.py

- Pequeños cambios estéticos en la estructura del código.

### app/comentario/models.py

- Pequeños cambios estéticos en la estructura del código.

### BlogIngoBase/

- Movida carpeta `static` a `BlogInfoBase/`

### BlogInfoBase/settings/base.py

- Eliminado código redundante en línea 132.
- Eliminada coma final en línea 134 debido a una incompatibilidad en el sistema de imágenes.

### BlogInfoBase/templates/base/base.html

- Solucionado error en línea 25; eliminado un Enter de sobra

### BlogInfoBase/templates/base/index.html

- Cambiada `src` de tag `img` en línea 12 a `{{post.img.url}}`

---

## Vesión (0.2.0) (04/12/21)

En esta versión se cambia la base de datos a SQLite para facilitar la transferencia de información entre el grupo. Esto se revertirá en la versión final.

### Cambios

### BlogInfoBase/

- Añadido `db.sqlite3`

### app/post/models.py

- Eliminado límite de caracteres en atributo `cuerpo`.

### BlogInfoBase/settings/local.py

- Agregada configuración de BD; cambiada a SQlite.

### .gitignore

- Línea 9; Eliminadas entradas: `db.sqlite3`, `db.sqlite3-journal`, `media` y `local_settings.py`.

---

## Vesión (0.3.0) (05/12/21)

### Cambios 

### BlogInfoBase/urls.py

- Añadida inclusión del archivo `urls.py` de la app `post` con su propio `namespace`.

### templates/base/index.html

- Cambio de `href` en ambas tags `a`; de `127.0.0.0:8000` a función `obtener_url_absoluta` del modelo `Post`.

### templates/post/post_simple.html

- Añadido `post_simple.html`; Un html súper simple que muestra información del post en cuestión.

### app/post/models.py

- Añadida función `obtener_url_absoluta`: Devuelve una URL para redireccionar al post en cuestión.
- Añadida función `__str__`.

### app/post/urls.py

- Añadido archivo `urls.py`; Espera una URL en forma de slug y devuelve la vista correspondiente.

### app/post/views.py

- Añadida vista `vista_post`. Será modificada en un futuro para agregar funcionalidad de comentarios.  

---

## Vesión (0.4.0) (07/12/21)

### Cambios 

### BlogInfoBase/templates/base/post/busqueda.html

- Agregado `busqueda.html`; será usado para mostrar los resultados de búsqueda.

### BlogInfoBase/templates/base/post/base.html

- Agregado `Block título`; permite cambiar el título de manera dinámica.
- Agregado `Block posts`; aísla la iteración de posts del `Block contenido`.

### BlogInfoBase/templates/base/post/index.html

- Agregada barra de navegación en `Block contenido`.

### app/post/models.py

- Solucionado pequeño error de comentario.

### app/post/views.py

- Modificada `inicio_view`; agregada funcionalidad para procesar request de búsqueda. 

---

## Versión (0.5.0-alpha) (09/12/21)

## Cambios

### BlogInfoBase/templates/base

- Reescritos archivos `base.html`, `footer.html`, `header.html` y `index.html`.

### app/post/admin.py

- Añadida opción de filtrado `destacado` en atributo `search_filters`.

### app/post/models.py

- Añadido atributo `destacado`; `BooleanField`. Usado para destacar el post.

### app/post/views.py

- Agregada variable `post_destacado`; Recibe el post destacado de la base de datos.
- Agregada lógica de búsqueda y filtrado de posts.
- Agregada variable `post_paginados`; Recibe los grupos de posts para mostrar en cada página provenientes de `p`.
- Actualizado `contexto`; Ahora es una variable aparte.

### app/utils/utils.py

- Agregada función `paginar`; Resuelve los números a mostrar en la barra de paginación del post.

### BlogInfoBase/db.sqlite3

- Agregados muchos posts de prueba, deben ser eliminados en la versión final.

---

## Version (0.6.0) (14/12/2021)

Primera versión que contiene el sistma de usuarios. Entre la versión 0.5.0-alpha y esta hubo muchos cambios, por lo que solo se muestra una vista general de lo que cambió.

### Cambios

### app/categoria/views.py

- Agregada `vista_categoria`

### app/categoria/urls.py

- Agregado `urls.py` con las url relacionadas.

### app/post/urls.py

- Agregadas urls relacionadas.

### app/post/views.py

- Agregadas views relacionadas.

### BlogInfoBase/settings/base.py

- Cambiado `language` de `en-us` a `es-es`

### templates/

- Agregados/modificados los archivos html.

---

## Version (0.7.0) (16/12/2021)

Version con cambios esteticos principalmente, se incluyó un html como modelo para la presentación de información en las categorías que se debe modularizar para una mejor optimizacíon.

### Cambios

### BlogInfoBase/templates/post/post_simplehtml

- se agrego una estructura para los post/categoría de ejemplo-

### BlogInfoBase/templates/footer.html

- se modificó el footer por problemas de compatibilidad con los nuevos cambios visuales.

### BlogInfoBase/templates/index.html

- se cambiaron aspectos visuales y se agregaron archivos de css y js. desde un template diferente al que ya teníamos con más opciones visuales.

---

## Version (0.8.0) (18/12/2021)

Es la primera versión que cumple con todos los requisitos.

### Cambios

### app/post/models.py

- Agregado atributo `numero_comentarios`.
- Agregado atributo `numero_visitas`.

### app/post/admin.py

- Se excluye la capacidad de edición de los nuevos atributos, y se los agrega en la vista de lista.

### app/post/urls.py

- Agregadas urls necesarias para acomodar los nuevos filtros.

### app/post/views.py

- Modificada `vista_paginada` para acomodar los nuevos filtros.
- Añadidas vistas `vista_fecha`, `vista_visitas` y `vista_comentarios`.
- Modificada `vista_inicio` para acomodar los nuevos filtros.
- Modificada `vista_post` para incrementar el `numero_visitas` y `numero_comentarios` según corresponda.

### app/utils/utils.py

- Agregado bloque Try/Except para lidiar con resultados de búsqueda vacíos.

### BlogInfoBase/templates/base/

- Modificado `index.html`
- Agregado `fecha.html` y `filtrado.html`

### BlogInfoBase/templates/post

- Modificado `paginacion.html`

---

## Versión (1.0.0) (20/12/21)

La versión final del proyecto.

## Cambios

- Retocados varios aspectos del proyecto, así como solucionados bugs menores y pulido ciertas cosas.

[//]: #
[Versionado Semántico 2.0.0]: <https://semver.org/lang/es/>
