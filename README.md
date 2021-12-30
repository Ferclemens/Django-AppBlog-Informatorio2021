# InfoBlog 
___
## Introducción

Este es el repositorio privado donde estaremos trabajando durante el desarrollo.
Este repositorio se mantendrá siempre privado, al momento de tener que presentar el proyecto, se abrirá un nuevo repositorio público con los archivos que sean absolutamente necesarios para evitar filtrar datos.
___
## _Primeros pasos_

Este repositorio contiene una instalación limpia de Django, es por esto que se deben configurar algunas cosas antes de comenzar a utilizarla.

## Instalando e iniciando el entorno virtual

Para asegurar la compatibilidad y autosuficiencia del código, es necesario crear un entorno virtual.


Una vez que tengamos creado un directorio de trabajo, se debe abrir una ventana del Símbolo del Sistema con privilegios de administrador en ese directorio y ejecutar el siguiente comando.
```sh
python -m venv env
```
Esto nos creará un entorno virtual utilizando [venv], y lo guardará en una carpeta llamada `env`


Una vez creado el entorno virtual, se lo debe iniciar con los siguientes comandos:

```sh
cd env\Scripts
activate.bat
cd..
cd..
```

> Nota: Es posible que este paso de un error si la política 
> de seguridad del sistema no permite la ejecución de scripts.
> De suceder, se debe ejecutar el siguiente comando en una 
> ventana de PowerShell con privilegios administrativos:  
> ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser```  
> Es común que solicite una confirmación, de ser así, se debe ingresar 
la letra `S` y presionar `Enter`.
> Esto además resolverá el problema si se presenta en el terminal
de Visual Studio Code.

Ahora, el entorno virtual está instalado y activado. No cierren este terminal, ya que nos servirá más adelante.

# Clonar el repositorio e instalar dependencias

En el directorio de trabajo, se debe crear una carpeta nueva.
El nombre de esta carpeta no importa y puede ser arbitrario, ya que solo sirve como un contenedor para ordenar mejor las cosas.

Una vez creada, se debe ingresar a la misma y ejecutar los siguientes comandos en un terminal GIT:


```sh
git init
git remote add origin https://github.com/maxacan/ProyectoDjangoInfo2021.git
git fetch origin
git checkout -b NombreDeRamaNueva
```
El último comando creará una rama nueva con el nombre que le demos, esto hace que tengamos una rama propia actualizada desde `main`.  

> Nota: El último comando se debe saltar si ya se creó una rama directamente desde GitHub.  
> Si se hizo eso, el comando se reemplaza por `git checkout NombreDeRamaCreada`.

Una vez clonado el código, se deben instalar las dependencias descriptas en el archivo `requeriments.txt`, ejecutando el siguiente comando en el terminal del Símbolo del Sistema que dejamos abierto, (debe estar posicionado en el directorio donde clonamos el código):


```sh
pip install -r requeriments.txt
```

# Creación de la base de datos, migración y creación de superuser

Ya tenemos todo lo que necesitamos para comenzar a utilizar Django, solamente faltan los últimos detalles:

A partir de la versión 0.2.0, el proyecto utiliza una base de datos de [SQLite] contenida en el archivo `db.sqlite`. Esto nos permite saltarnos la creación de la misma y asegurarnos de que los datos estén incluidos en cada rama.

Además, ya se encuentra configurado un `superuser` con las siguientes credenciales:

- *Usuario* : `root`
- *Contraseña* : `root`

De todas maneras, podemos crear un nuevo `superuser` de la siguiente manera:

Asegurandonos de que esté activado el entorno virtual, desde el terminal de Visual Studio Code ejecutamos el comando: 
```sh
python .\manage.py createsuperuser
```

Esto nos dará un pequeño programa interactivo que nos pedirá ingresar un usuario, un correo electrónico y una contraseña.

Si presionamos enter sin haber ingresado nada cuando nos pide un usuario, el usuario se convierte en el nombre de usuario del sistema. De lo contrario, podemos ingresar el usuario que queramos, el cual se recomienda que sea sencillo, ya que se va a estar usando constantemente y escribir un usuario complicado cada vez que se necesite entrar al panel de administración se vuelve muy tedioso, muy rápido.


Luego, nos pide un correo, el cual puede estar en blanco, ya que no se usa para acceder al panel administrativo.

La contraseña puede ser arbitraria, aunque si Django detecta que es una contraseña muy sencilla, como `12345`, nos mostrará un mensaje preguntando si queremos confirmar o no el uso de la misma, si nos aparece este mensaje, simplemente escribimos `y` y presionamos `Enter`.
Como con el usuario, se recomienda una contraseña sencilla para que no se vuelva tedioso el trabajo de entrar al panel administrativo.

# Pasos finales

Lo único que resta hacer para confirmar que todo funcione correctamente, es ejecutar el comando:
```sh
python .\manage.py runserver
```
Este comando abre el servidor en la dirección `127.0.0.1:8000/`.

Si nos vamos a esa dirección en nuestro navegador, deberíamos ver la página por defecto de Django, con la leyenda:  
`The install worked successfully! Congratulations!`

[//]: #
[venv]: <https://docs.python.org/es/3/library/venv.html>
[SQLite]: <https://www.sqlite.org/about.html>

