# Ejercicios Tema 5

## Ejercicio 1

Instalar los paquetes necesarios para usar KVM. Se pueden seguir estas instrucciones. Ya lo hicimos en el primer tema, pero volver a comprobar si nuestro sistema está preparado para ejecutarlo o hay que conformarse con la paravirtualización.

Siguiendo el tutorial:

- apt install qemu-kvm libvirt-clients qemu-utils libvirt-daemon-system
- adduser <youruser> libvirt
- adduser <youruser> libvirt-qemu

## Ejercicio 2

1. Crear varias máquinas virtuales con algún sistema operativo libre tal como Linux o BSD. Si se quieren distribuciones que ocupen poco espacio con el objetivo principalmente de hacer pruebas se puede usar CoreOS (que sirve como soporte para Docker) GALPon Minino, hecha en Galicia para el mundo, Damn Small Linux, SliTaz (que cabe en 35 megas) y ttylinux (basado en línea de órdenes solo).

Usamos la siguiente orden para ir creando las diferentes maquinas virtuales:

- qemu-system-x86_64 -hda /media/Backup/Isos/discovirtual.img -cdrom ~/tmp/debian-7.3.0-i386-netinst.iso

La opción -hda indica el fichero en el que se va a alojar el sistema operativo instalado y -cdrom recibe el camino a la ISO en la que está el sistema que se va a instalar, en nuestro caso con los sistemas virtuales mencionados en el ejercicio.

2. Hacer un ejercicio equivalente usando otro hipervisor como Xen, VirtualBox o Parallels.

Para hacerlo con VirtualBox, hay dos opciones: usando Vagrant o manualmente desde la interfaz. Desde la interfaz, vamos siguiendo los pasos que nos indica:

- Seleccionar el iso con el SO.
- Seleccionar las especificaciones de memoria, RAM, etc.

Desde vagrant, usamos el terminal para crear una maquina virtual:

- vagrant init SO

En SO, especificamos el sistema operativo con el que queremos iniciar nuestra MV.

## Ejercicio 3

Crear un benchmark de velocidad de entrada salida y comprobar la diferencia entre usar paravirtualización y arrancar la máquina virtual simplemente con "qemu-system-x86_64 -hda /media/Backup/Isos/discovirtual.img"

Ejecutamos la siguiente orden para crear el benchmark:

- qemu-system-x86_64 -boot order=c -drive	file=/media/Backup/Isos/discovirtual.img,if=virtio

Una vez creado el benchmark, podemos ejecutar la orden "qemu-system-x86_64 -hda /media/Backup/Isos/discovirtual.img", y se iniciará nuestra MV de forma más rápida.

## Ejercicio 4

Crear una máquina virtual Linux con 512 megas de RAM y entorno gráfico LXDE a la que se pueda acceder mediante VNC y ssh.

Usando VirtualBox, instalamos SparkyLinux con las especificaciones indicadas. Una vez accedamos a la máquina virtual, instalamos ssh en ella y, obviamente, tenemos que tener ssh instalado en nuestra máquina anfitriona.

Podemos ver con vinagre, como al crear un archivo en la máquina anfritiona mediante ssh. nos aparece en la MV.

## Ejercicio 5

Crear una máquina virtual Ubuntu e instalar en ella alguno de los servicios que estamos usando en el proyecto de la asignatura.