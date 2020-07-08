COMANDOS LINUX

# mostrar la fecha del sistema
date

# mostrar el manual de un comando
man {comando}

# imprimir un mensaje
echo "{mensaje}"

# muestra el historial de comandos del sistema
history

# vuelve a ejecutar un comando del historial usando el NRO identificador
!{nro_id}

# mostrar archivos
ls
ls -a # mostrar todos los archivos, incluyendo ocultos
ls -l # mostrar los archivos como una lista
ls -lh # lo mismo de arriba pero con las unidades de tamaño medidas en KB, MB
ls -R # muestra el contenido también de los directorios de forma recursiva
ls -t # ordena los archivos por fecha de modificación
ls -x # ordena los archivos por nombre y después por extensión
ls -S # ordena los resultados por tamaño de archivo

# mostrar directorio donde estamos trabajando
pwd

# cambiar directorio de trabajo
cd {ruta_directorio}
cd ~ # lleva al directorio home del usuario 
cd .. # retroceder un nivel en el arbol de directorios
cd - # retrocede al último directorio visitado
cd / # lleva a la raíz del árbol de directorios

# crear un directorio en el directorio donde se está trabajando
mkdir {nombre_del_directorio}

# copiar archivos
cp {nombre_o_ruta_archivo} {ruta_destino}

# mover archivo
mv {nombre_o_ruta_archivo} {ruta_destino}

# borrar archivo
rm {nombre_o_ruta_archivo}

# eliminar directorio
rmdir {nombre_o_ruta_directorio}

# abrir editor de texto
vi
vim
nano

# crear un archivo
touch {nombre_extension_archivo_nuevo}

# mostrar contenido archivo
cat {nombre_o_ruta_archivo}

# mostrar contenido archivo al revés
tac {nombre_o_ruta_archivo}

# mostrar las primeras líneas de un archivo
head {nombre_o_ruta_archivo}
head -n 10 {nombre_o_ruta_archivo} # muestra sólo diez primeras lineas

# mostrar las últimas líneas de un archivo
tail {nombre_o_ruta_archivo}
tail -n 10 {nombre_o_ruta_archivo} # muestra sólo diez ultimas lineas

# buscar por expresiones regulares
grep {expresion_regular} {nombre_o_ruta_archivo}
grep -i {expresion_regular} {nombre_o_ruta_archivo} # insensible a mayúsculas y minusculas
grep -i "{expresion_regular}$" {nombre_o_ruta_archivo} # insensible a mayúsculas y minusculas, busca la expresión al final de cada línea
grep "^{expresion_regular}" {nombre_o_ruta_archivo} # busca la expresión al principio de cada línea

# Buscar texto dentro de archivos, por ejemplo, buscamos la palabra "texto" dentro de todos los archivos de texto (.txt) que tengamos en el directorio "home":
grep "texto" /home/ *.txt

# Si queremos buscar en ese directorio y en los que están dentro de él:
grep -r "texto" /home/ *.txt

# Buscar en ese directorio, en los que están dentro de él y en cualquier tipo de archivo:
grep -r "texto" /home/

# Tratamiento de flujo de caracteres (no modifica archivo)
sed 's/{texto_viejo}/{texto_nuevo}/g' {nombre_o_ruta_archivo}

# tratamiento de texto delimitado por un carácter (pueden ser comas, tabuladores, etc)
awk -F '{caracter_delimitador}' '{ print $1 }' {nombre_o_ruta_archivo} # imprime hasta el primer carácter delimitador que encuentre de cada columna

# guardar salida estándar de un comando en un archivo nuevo
{comando} > {nombre_extension_archivo_nuevo}

# agregar salida estándar al final de un archivo existente
{comando} > {nombre_extension_archivo_existente}

# muestra archivos grandes
more

# cuenta palabras o líneas
wc 

# direccionar la salida estándar de un comando a otro comando
{comando} | {comando)
ls -l | more # muestra el resultado largo en varias iteraciones
cat {nombre_o_ruta_archivo} | wc -l # pasa el resultado del cat al comando "wc" que cuenta las lineas

# mostrar procesos del usuario
ps
ps ax # muestra todos los procesos del sistema

# muestra los procesos en modo interactivo
top

# matar un proceso corriendo en primer plano 
[ctrl] + c

# matar a un proceso en segundo plano
kill -9 {identificador_del_proceso}










CONFIGURACION TARJETA RED-
#ifconfig = comando para obtener informacion sobre la red (direccion ip,mascara,direccion mac etc)
#system-config-network-tui = interfaz grafica de red 
#/etc/init.d/network restart = reinicio de interfaces de red

VERIFICAR FICHEROS RED
#cd /etc/sysconfig/network-scripts/
#cat ifcfg-eth0
ip route show= puerta de enlace
cat etc/resolv.conf=muestra dns


PARTICIONES COMUNES
#fdisk -l | more = para mostrar discos en el sistema
#df -k = para visualizar particiones activas en el sistema
#hdparm -I /dev/sdb | more = revisar parametros del disco agregado

CREANDO PARTICION EN DISCO----
#fdisk /dev/sdb = crea una nueva particion en el disco
apretar "m" para ver las opciones de fdisk
seleccionar "n" para crear una nueva particion 
primero elegir si es extendida(e) o primaria (p) elegir letra luego enter
numero de particion 
elegir cilindro
y elegir el valor de la particion ej +4G
grabar laconfiguracion con "w"

ver particiones creadas nuevamente = fdisk –l | more
se crea /dev/sdb1********
DAR SISTEMA DE ARCHIVOS A PARTICION
# mke2fs –j /dev/sdb1 
//extendido2 por defecto para otros tipos usar = mkfs -t ext4 /dev/sdb1 O mkfs.ext4 
#blkid /dev/sdb1 verificar que tipo de sistema de archivos tiene la particio
Crear directorio para montar 
#cd /
#mkdir /disco1
Montar particion en el directorio creado
#mount /dev/sdb1 /disco1
# df –k = muestra  donde esta montado

CREAR ARCHIVO PARA CONFIRMAR(OPCIONAL)
#cd /disco1
#touch  archivo.txt 
#ls si muestra esta bien

MONTAJE PERMANENTE EDITANDO nano /etc/fstab
EJEMPLO
/dev/sdb1		/disco1		auto	defaults	0 0


ELIMINAR SISTEMA DE ARCHIVOS
1. Desmontar el sistema de archivos mediante umount /mountpoint.
2. Quite la entrada correspondiente en /etc/fstab.
3. Quite el direc
torio de punto de montaje: rmdir /mountpoint.


LVM

# fdisk –l | more = verificar unidades nuevas
Cree los Phisycal Volume 
# pvcreate /dev/sdb
# pvcreate /dev/sdc

Cree un Volume Group llamado “vgduoc” 
# vgcreate vgprueba /dev/sdb
# vgextend vgprueba /dev/sdc
Confirmar VG CORRECTO
#vgdisplay nombre_vg

CREAR VOLUMEN LOGICO 
#lvcreate –n nombre_lv --size tamaño nombre_vg 
EJ:lvcreate -n lvprueba --size 2048M vgprueba
CONFIRMAR LA CREACION:
# lvdisplay /dev/nombre_vg/nombre_lv
EJ: lvdisplay /dev/vgprueba/lvprueba
CREAR SISTEMA DE ARCHIVOS PARA LV:
# mke2fs /dev/nombre_vg/nombre_lv
PUNTO DE MONTAJE, MONTAR EL LV Y CONFIRMACION
#mkdir /lvmontaje
#mount /dev/vgprueba/lvprueba /lvmontaje/
#df -k = VERIFICAR SI ESTA MONTADO

REDUCCION DE SISTEMA DE ARCHIVOS Y VOLUMEN LOGICO
#umount /lvmontaje
#lvreduce -L -1024 /dev/vgprueba/lvprueba
# e2fsck –f /dev/vgprueba/lvprueba
# resize2fs /dev/nombre_vg/nombre_lv

AUMENTAR VOLUMEN LOGICO
#umount /lvmontaje
#lvextend -L +2048 /dev/vgprueba/lvprueba
#e2fsck –f /dev/vgprueba/lvprueba
#resize2fs /dev/vgprueba/lvprueba

Obtenga información del PV, VG y LV con los siguientes comandos:
# pvdisplay /dev/sdb

Elimine el LV siguiendo el siguiente procedimiento:
- desmonte las particiones del LVM
- borre el VG
- borre el PV

#umount /lvmontaje
#vgremove vgprueba
preguntara si decea eliminar los lv decir que "y"
#pvremove /dev/sdb
#pvremove /dev/sdc


TAREAS PROGRAMADAS CROTAB
ver archivo 
#cat /etc/crontab
EDITAR
#nano /etc/crontab

orden:
-minutos-horas-dias del mes-meses-dia de la semana-usuario-comando


----------APACHE(WEB)------------
#yum install httpd = instala servicio

#chkconfig httpd on = activa servicio en todos los niveles
SERVICIO
#service httpd start =activa
#service httpd restart = reinicia
#service httpd reload = carga los cambios
#service httpd stop = detiene

EDITAR DIRECTIVAS 
gedit /etc/httpd/conf/httpd.conf

BUSCAR Y EDITAR
SERVERNAME www.prueba.cl:8080
DOCUMENTROOT "var/www/html/prueba"  = donde se encuentran los archivos web
LISTEN 8080

gedit /etc/hosts  = editar host y puertos 
Abrir firewall http & https

CREAR DIRECTORIO
mkdir /var/www/html/prueba

CREAR INDEX .HTML
nano /var/www/html/prueba/index.html
<html>
<head>
<title>WEB</title>
</head>
<body bgcolor=lightblue>
<h2>Bienvenido WEB</h2>
</body>
</html>



----------USUARIOS Y GRUPOS----------------
USUARIOS
#useradd = Creación de usuarios 
#usermod = Modificación de usuarios
#userdel = Eliminación de usuarios 

GRUPOS
#groupadd  = Creación de grupos 
#groupmod = Modificación de grupos 
#groupdel = Eliminación de grupos 


#id usuario = detalles sobre el usuario
#groups [usuario] = La orden groups muestra la pertenencia al grupo
# gpasswd -a [usuario] [grupo] = Puede agregar un usuario a un grupo 
# gpasswd -d [usuario] [grupo] = Puede eliminar un usuario de un grupo
# passwd [nombredeusuario] = Para especificar la contraseña del usuario
  
#cat /etc/shadow	= Información reservada de las cuentas de usuario
#cat /etc/passwd	= Información de las cuentas de usuario
#cat /etc/gshadow	= Contiene información reservada de los grupos de usuarios
#cat /etc/group	 = Define a que grupos pertenecen los usuarios
#cat /etc/sudoers	= Lista lo que se puede ejecutar con sudo
#cat /home/*	= Carpeta personal del usuario

#su usuario = permite cambiar el usuario
#su = cambia por usuario root
#newgrp grupo  = permite cambiar el grupo primario del usuario actual


------------PROPIEDADES ARCHIVOS Y PERMISOS
lectura (r), escritura (w) y ejecución (x)
(r) tiene 4, 
 w) tiene 2, 
 x) tiene 1. 
 
#chmod 777 archivo = cambia permisos de archivo
#chgrp gruponuevo archivo = cambia de grupo propietario el archivo
#chown usuario archivo = cambia usuario propietario del archivo

chmod = lo puede usar: root y el propietario del archivo
chgrp = lo puede usar ;root y el propietario de archivo (únicamente los grupos subscritos)
chown = lo puede usar: root

umask = permisos predeterminados
#umask 777 = nuevos permisos predeterminados
 

---------- SERVICIOS ----------------

	# Validacion de paquetes instalados
	rpm -aq | grep paquete
	yum list installed | grep wget

	## Servicios

		# informacion del servicio 
		systemctl help servicio

		# consultar dependencias del servicio o una unidad
		systemctl list-dependencies servicio

		# servicios que se usarán después de iniciar un servicio
		systemctl list-dependencies --before cron

		# iniciar servicio
		systemctl start servicio

		# status de un servicio
		systemctl status servicio

		# reiniciar servicio
		systemctl restart servicio

		# recargar configuracion de un servicio sin reiniciarlo
		systemctl reload servicio

		# detener un servicio
		systemctl stop servicio

		# arranque de forma automática al iniciar el ordenador
		systemctl enable servicio

		# que al arrancar el ordenador no se cargue un servicio
		systemctl disable servicio

		# enmascarar un servicio: que no se pueda iniciar manualmente ni automáticamente después de iniciar la sesión
		systemctl mask servicio

		# desenmascarar un servicio
		systemctl unmask servicio



		
# Ver cuanto pesa un archivo en MB
du -h nombre_archivo


# Desplegar programas instalados en linux
dpkg-query -l

# Desplegar programas instalados en linux, solo los nombres, sin mostrar la version ni descripcion
dpkg-query -f '${binary:Package}\n' -W

# Buscar en el cache de apt programas que calcen con python3-pip
apt-cache search python3-pip

#######################################################################################################
init
#######################################################################################################
The best solution to know about these init levels is to understand the ” man init ” command output on Unix.
There are basically 8 runlevels in unix. I will briefly tell some thing about the different init levels and their use.
Run Level:  At any given time, the system is in one  of  eight  possible run  levels.  A  run level is a software configuration under which only a selected group of processes  exists.  Processes spawned  by init for each of these run levels are defined in /etc/inittab. init can be in one of eight  run  levels,  0-6 and  S  or  s (S and s are identical). The run level changes when a privileged user runs /sbin/init.
init 0 :  Shutdown (goes thru the /etc/rc0.d/* scripts then halts)
init 1  :  Single user mode or emergency mode means no network no multitasking is present in this mode only root has access in this runlevel
init 2  :  No network but multitasking support is present .
init 3  :  Network is present multitasking is present but with out GUI .
init 4  :  It is similar to runlevel 3; It is reserved for other purposes in research.
init 5  :  Network is present multitasking and GUI is present with sound etc.
init 6  :  This runlevel is defined to system restart.
init s   : Tells the init command to enter the maintenance mode. When the
system enters maintenance mode from another run level, only the system console
is used as the terminal.
init S  : Same as init s.
init m : Same as init s and init S.
init M : Same as init s or init S or init m.
We can take it from above that 4 options(S,s,M,m) are synonymous.
#######################################################################################################




PROCESOS

# correr un proceso en segundo plano
{comando} &



# ver procesos corriendo en la capa de usuario
jobs

# traer adelante la ejecucion de el proceso 1 corriendo en background
fg 1

# llevar para atras la ejecucion de el proceso 1 y dejarlo corriendo
bg 1

# quitar la propiedad del proceso
disown





BUSQUEDA

# buscar la cadena entre comillas en el directorio solo en los archivos de extension html
grep "nombre_tarea_grace" /var/doc_alert/web_doc_alert/core/templates/core/ *.html







VARIABLES DE ENTORNO

# para declarar una variable de entorno local se usa el nombre de la variable, signo igual, valor de la variable
nombre_variable=valor

# para eliminar una declaracion de variable de entorno se usa el comando unset, espacio, el nombre de la variable
unset nombre_variable

# para setear una variable GLOBAL (es decir, que este disponible para todo el sistema, no solo para el shell actual)
# de entorno se usa el comando export, espacio, nombre de la variable (mayusculas es el estandar), signo igual, valor
export NOMBRE_VARIABLE=valor

# para imprimir el contenido de una variable de entorno especifica se usa el comando echo, espacio, signo peso, nombre de la variable
echo $NOMBRE_VARIABLE

# para imprimir el contenido de todas la variables de entorno se usa el comando env o printenv
env
# o
printenv

# algunas variables estandar de linux son las siguientes
DISPLAY		# Donde aparecen la salidas de X-Windows.
HOME		# Directorio personal.
HOSTNAME	# Nombre de la máquina.
MAIL		# Archivo de correo.
PATH		# Lista de directorios donde buscar los programas.
PS1		# Prompt.
SHELL		# Intérprete de comandos por defecto.
TERM		# Tipo de terminal.
USER		# Nombre del usuario.






HARDWARE & SOFTWARE INFO

lscpu
lshw
hwinfo
lspci
lsscsi 
lsusb
lsblk 
inxi -Fx
df -H
fdisk -l
dmidecode -t processor
dmidecode -t memory
dmidecode -t bios

hostnamectl

hdparm -i /dev/sda
uname -a
lsb_release -a

cat /etc/os-release
cat /etc/issue
cat /proc/version
cat /etc/*-release
cat /etc/debian_version
cat /proc/cpuinfo
cat /proc/meminfo
cat /proc/version
cat /proc/scsi/scsi
cat /proc/partitions 


