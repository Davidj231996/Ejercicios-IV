# Ejercicios Tema 1

## Ejercicio 1

Descargar y ejecutar las pruebas de alguno de los proyectos anteriores, y si sale todo bien, hacer un pull request a alguno de esos proyectos con tests adicionales, si es que faltan (en el momento que se lea este tema).

Para realizar este ejercicio, solo necesitamos descargar uno de los archivos de test y ejecutarlos mediante python *nombre_archivo*.

## Ejercicio 2

Para la aplicación que se está haciendo, escribir una serie de aserciones y probar que efectivamente no fallan. Añadir tests para una nueva funcionalidad, probar que falla y escribir el código para que no lo haga (vamos, lo que viene siendo TDD).

Como podemos ver en nuestro archivo de [tests](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/src/test_noticiario.py), tenemos varios asserts realizados, y realizando python *nombre_archivo* podemos observar su funcionamiento.

## Ejercicio 3

Crear algún conjunto de scripts de tests, usando tu lenguaje favorito, y ejecutarlos desde el marco de test más adecuado (o el que más te guste) para ese lenguaje.

Podemos observarlo en el mismo [archivo](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/src/test_noticiario.py) mencionado anteriormente.

## Ejercicio 4

Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).

En nuestro caso vamos a hacerlo en python, y se realiza con la siguiente orden:

[sudo] pip install virtualenv

## Ejercicio 5

Este ejercicio esta resuelto en el archivo [empresa.py](https://github.com/Davidj231996/Ejercicios-IV/blob/master/Tema2/empresa.py)

## Ejercicio 6

Si usamos versiones antiguas de python, no funciona debido a que hay funcionalidades no incluidas.

## Ejercicio 7

Crear una descripción del módulo usando package.json. En caso de que se trate de otro lenguaje, usar el método correspondiente.

En python podemos usar el módulo pip, y con un [archivo txt](https://github.com/Davidj231996/Proyecto-Vengadores/blob/master/requirements.txt) en el que le ponemos las necesidades. La orden sería la siguiente: *pip install -r requirements.txt*

## Ejercicio 8

Automatizar con grunt, gulp u otra herramienta de gestión de tareas en Node la generación de documentación de la librería que se cree usando docco u otro sistema similar de generación de documentación. Previamente, por supuesto, habrá que documentar tal librería.

Para python podemos encontrar Sphynx, que se instala de la siguiente forma: *easy_install -U sphinx*.

## Ejercicio 9

![Travis](/Capturas/travis.png)