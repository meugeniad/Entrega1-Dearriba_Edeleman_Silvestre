PROYECTO : Entrega1-Dearriba_Edeleman_Silvestre
Descripción:

Nuestro proyecto es un blog de turismo que permitan orientar de manera sencilla a distintos tipos de turistas para poder cumplir con sus sueños.

Autores:
- María Eugenia Dearriba (CRUD de destinos)
- Pablo Silvestre (módulo de seguridad)
- Laura Edelman (buscador en destinos - Readme - Inicio - Nosotros)

Descripción de Nuestra Página de Viajes
***************************************
Menú Principal:

  - Inicio         : Al acceder por primera vez se posiciona en la vista inicial. La misma intenta dar un resumen de nuestro sentir por recorrer el mundo.
  - Nosotros       : Te acercamos información de quienes estamos comprometidos con este nuevo y esperanzador proyecto.
  - Agregar Destino: Nos permite sumar a nuestra base de datos paises y ciudades, con detalles de lugares especiales y sugerencias muy personalizadas. Se debe estar logueado como usuario
  - Ver destinos   : Alli se podrá mostrar todos los lugares que como equipo hemos investigado para tu mejor opción como así también la posibilidad de una búsqueda
                   particular por país. Desde esta opción se puede Eliminar o Modificar un destino para lo cual se debe estar logueado como usuario
  Sin usuario logueado
  - Iniciar Sesión: sirve para loguearse como usario
  - Registrarse: sirve para darse de alta como usuario

  Con usuario logueado:
  - Usuario: nombre_usuario: muestra los datos del usuario y permite modificar y cambiar la contraseña
  - Cerrar sesión: sirve para hacer logout

  Sin acceso por menú: el módulo de administración no tiene acceso por menú, solo por url completa "http://127.0.0.1:8000/admin/"

Instalación y Pruebas
*********************
- Pre Requisito : Tener Git Instalado - Tener el link de nuestro repositorio en GitHub

  1 . Crear carpeta local.
  
  2 . Iniciar Visual Code.
  
  3 . Abrir terminal.
  
  4 . Posicionarte en la carpeta creada. Fijate bien de estar allí con un dir o ls.
  
  5 . Acceder al link del GitHub que te hemos pasado.
  
  6 . Mediante el botón "Code" de HitGub copiar las sentencias necesarias para Clonar.
  
  7 . En la terminal poner git clone <url copiada en paso 6>
  
  8 . Crear entorno virtual desde el archivo start.sh o si lo haces por linea de comando fijate en el .ignore que alli está su nombre.
  
  9 . Instalar Django en el entorno virtual pip install -r reuirements.txt
  
  10 . Ejecutar las migraciones py manage.py makemigrations - py manage.py migrate
  
  11 . Levantar el servicio py manage.py runserver y accedes mediante ctrl + click a la url local indicada.
  
  12 . Probar cada opción descripta en la descripción de nuestra página.
    
Pruebas
***************
- Intentar ver destinos sin estar logueado: debe permitirlo
- Intentar editar o eliminar o agregar un destino sin estar logueado: debe llevar a la página para loguearse


  
