# Ejercicios Tema 1

- Ejercicio 1: Consultar en el catálogo de alguna tienda de informática el precio de un ordenador tipo servidor y calcular su coste de amortización a cuatro y siete años. 
[Consultar este artículo en Infoautónomos sobre el tema.](https://infoautonomos.eleconomista.es/consultas-a-la-comunidad/988/)


![Servidor](/Capturas/Servidor.png)

Vamos a usar dicho ordenador como servidor. Dicho ordenador tiene un coste de 1559€, siguiendo el link proporcionado por el profesor vamos a calcular su amortización en 4 y 7 años.

- - 4 años.

Para poder amortizarlo en 4 años, debemos de comprarlo antes de la mitad de año, para que así podamos amortizar por completo el ordenador y no la mitad. Además, el máximo porcentaje de 
amortización por año es de 25%.

1. Primer año: 389.75€
2. Segundo año: 389.75€
3. Tercer año: 389.75€
4. Cuarto año: 389.75€

- - 7 años

En este caso si podríamos comprar el ordenador en la segunda mitad del año, estudiaremos ambos casos. Primero, si lo compramos en la primera mitad:

Supondremos una amortización del 15% los seis primeros años, y en el séptimo la amortización final restante.

1. Primer año: 233.85€
2. Segundo año: 233.85€
3. Tercer año: 233.85€
4. Cuarto año: 233.85€
5. Quinto año: 233.85€
6. Sexto año: 233.85€
7. Séptimo año: 155.90€

Si lo compramos en la segunda mitad:

Supondremos una amortización del 16%, el primer año sería del 8% y el séptimo año sería la amortización restante.

1. Primer año: 124.72€
2. Segundo año: 249.44€
3. Tercer año: 249.44€
4. Cuarto año: 249.44€
5. Quinto año: 249.44€
6. Sexto año: 249.44€
7. Séptimo año: 187.08€

- Ejercicio 2: Usando las tablas de precios de servicios de alojamiento en Internet “clásicos”, es decir, que ofrezcan Virtual Private Servers o servidores físicos, y de proveedores de 
servicios en la nube, comparar el coste durante un año de un ordenador con un procesador estándar (escogerlo de forma que sea el mismo tipo de procesador en los dos vendedores) y con 
el resto de las características similares (tamaño de disco duro equivalente a transferencia de disco duro) en el caso de que la infraestructura comprada se usa sólo el 1% o el 10% del 
tiempo.


![Amazon EC2](/Capturas/Amazon.png)

![Dinahosting](/Capturas/Dinahosting.png)

He encontrado dos vps, uno con coste variable dependiendo del uso(Amazon EC2) y otro con una cuato fija(Dinahosting). Voy a comprobar la diferencia de precio entre ambas ofertas:

El precio de la cuota fija de Dinahosting es de 180.00€ mensuales. Un mes tiene 720 horas (suponiendo que 1 mes tiene 30 dias). El precio por hora en Amazon es de 0.192$ ~= 0.16€

- - 1% de uso

Un 1% de 720 horas mensuales son 7,2 horas de uso. Lo que conlleva a un coste de 8*0.16 = 1.28€/mes. Una diferencia de 178.72€.

- - 10% de uso

Un 10% de 720 horas mensuales son 72 horas de uso. Lo que conlleva a un coste de 72*0.16 = 11.52€/mes. Una diferencia de 168.48€.


- Ejercicio 3: En general, cualquier ordenador con menos de 5 o 6 años tendrá estos flags. ¿Qué modelo de procesador es? ¿Qué aparece como salida de esa orden? Si usas una máquina 
virtual, ¿qué resultado da? ¿Y en una Raspberry Pi o, si tienes acceso, [el procesador del 
móvil?](https://stackoverflow.com/questions/26239956/how-to-get-specific-information-of-an-android-device-from-proc-cpuinfo-flie)

![Procesador](/Capturas/Procesador.png)

![Resultado de la orden](/Capturas/Orden.png)

En estas imágenes podemos observar el procesador de mi portátil y el resultado de ejcutar la orden "egrep '^flags.*(vmx|svm)' /proc/cpuinfo".

![Orden en Máquina Virtual Ubuntu](/Capturas/Orden_Ubuntu.png)

En esta imágen, hemos buscado el archivo /proc/cpuinfo en una máquina virtual con Ubuntu 14.04. Podemos observar que el procesador es el mismo, pero que los flags cambian.

Tras un poco de investigación, no he podido encontrar nadie que me diga como acceder a un archivo como el cpuinfo en un dispositivo iOS.

- Ejercicio 4:

1. Comprobar si el núcleo instalado en tu ordenador contiene este módulo del kernel usando la orden "kvm-ok".

![KVM-OK](/Capturas/kvm.png)

En la imágen podemos ver que el comando no existe, por lo que no tengo instalado ese módulo del kernel.

2. Instalar un hipervisor para gestionar máquinas virtuales, que más adelante se podrá usar en pruebas y ejercicios.

![Instalación de QEMU](/Capturas/QEMU.png)

- Ejercicio 5: Darse de alta en servicios de nube usando ofertas gratuitas o cupones que pueda proporcionar el profesor.

![Amazon EC2](/Capturas/EC2.png)
![Azure](/Capturas/Azure.png)

A pesar de ser pruebas gratuitas, en ambos casos nos piden la tarjeta de crédito. Tras realizar una pequeña investigación, he descubierto el porque de pedir las terjetas de crédito. 
Nos piden las tarjetas, debido a que, a pesar de ser pruebas gratuitas, dichas pruebas tienen un límite de trabajo, y en el caso de sobrepasar dichos límites, tendríamos que pagar por 
lo gastado. Debido a que no dispongo de otra tarjeta de crédito para usar en estos casos, e intentar evitar la carga del precio de dichos servicios, no he podido seguir.

- Ejercicio 6: Darse de alta en una web que permita hacer pruebas con alguno de los sistemas de gestión de nube anteriores.

![OpenStack](/Capturas/Openstack.png)
