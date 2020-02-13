COMANDOS LINUX

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





