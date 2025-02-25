COMANDOS LINUX
#######
# QoL #
#######
# Editar archivo de configuracion de vim 
vim  ~/.vimrc

# Enchular cat a batcat
# Isntalacion
sudo apt install bat
# Link simbolico a bat
sudo ln -s /usr/bin/batcat /usr/local/bin/bat
# Elegir tema
export BAT_THEME="Monokai Extended"
echo "export BAT_THEME="Monokai Extended" >> ~/.bashrc 


# Enchular vim 
cat <<EOF > ~/.vimrc
syntax on
colorscheme desert
set number
set cursorline
set history=1000
EOF

### SUBLIME TEXT STYLE
# descargar estilo
cd ~/.vim/colors
curl -o molokai.vim https://raw.githubusercontent.com/tomasr/molokai/master/colors/molokai.vim
# actualizar configuracion de vim
cat <<EOF > ~/.vimrc
syntax on
colorscheme desert
set number
set cursorline
set history=1000
EOF


# mostrar la fecha del sistema
date

# mostrar el manual de un comando
man {comando}

# imprimir un mensaje
echo "{mensaje}"

# muestra el historial de comandos del sistema
history

# para que el history se muestre con un timespan
export HISTTIMEFORMAT='%F %T : '

# para que se vuelva permanente lo de arriba
echo "export HISTTIMEFORMAT='%F %T : '" >> $HOME/.bashrc



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

ls -ali
+--------------+------------------+-----------------+-------+-------+------+-------+-----+-------+-----------+
| index number | file permissions | number of links | owner | group | size | month | day | time  | filename  |
+--------------+------------------+-----------------+-------+-------+------+-------+-----+-------+-----------+
|       933442 | -rwxrw-r--       |              10 | root  | root  | 2048 | Jan   |  13 | 07:11 | afile.exe |
+--------------+------------------+-----------------+-------+-------+------+-------+-----+-------+-----------+

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

# mostrar las primeras lineas de un archivo
head {nombre_o_ruta_archivo}
head -n 30 {nombre_o_ruta_archivo} # muestra sólo 30 primeras lineas

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

# buscar en todo el sistema de archivos, no sirve para buscar archivos nuevos, ya que la BD se tiene que actualizar periodica y explicitamente
locate hello.php

# para actualizar la BD de locate
updatedb

# ubicar archivos binarios (o comandos)
whereis {comando}

# busqueda compleja dentro de un arbol de directorios, donde XXX son los permisos del archivo buscado
find {path} - user {usuario} -perm {XXX}

# buscar archivos en mi directorio actual (.) que sean del usuario shalo que tengan los permisos 644
find . -user shalo -perm 644

# buscar solo archivos modificados en un intervalo de tiempo (hace mas de siete dias)
find . -type f -mtime +7

# buscar solo archivos modificados en un intervalo de tiempo (hace mas de siete dias), y aparte ejecutar un copiado al directorio /backup
find . -type f -mtime +7 -exec cp {} ./backup/ \;

# realizar una peticion http a una pagina web
curl http://pagina.com

# descargar un archivo de un sitio remoto
wget http://pagina.com/archivo.txt

# enviar email 
echo "{text del mail}" | mail -s "{asunto del mail}" correo@mail.com

# imprimi variable de entorno
echo $NOMBRE_VARIABLE

# asignar valor a una variable de entorno durante toda la sesion
export NOMBRE_VARIABLE={valor}

# asignacion particular de una variable ya seteada (modificacion)
NOMBRE_VARIABLE={valor}

# ejecutar una tarea dentro de 2 minutos a partir de ahora
at now +2 minutes [enter]
echo "Usando comando at" > /home/shalo/prueba.txt

# ver la tabla de tareas programadas
crontab -l

# editar la tabla de tareas programadas
crontab -e

# easter egg o huevo de pascua, del programador de apt LOL
apt-get moo

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

# mostrar los alias
alias

# obtener un hash de un archivo usando el algoritmo sha256
sha256sum archivo.txt

# leer archivos grandes
less archivote.txt

# limpiar consola/pantalla
clear
# o
[ctrl] + L

     
	     
# sacar imagen, dumpeo de data
dd if=/dev/sdb of=/ruta/destino/archivodestino

# imagen forense en partes de 300megabytes calculando hash md5 y sha1, con el modo interactivo activado para que actualize en pantalla lo que hace
# ademas guarda un log
dc3dd if=/dev/sdb hofs=/ruta/destino/archivodestino ofsz=300MB hash=md5 hash=sha1 verb=on log=/ruta/destino/archivolog.txt	     

# validar estado general del sistema
htop
	     
# mostrar interfaces de red
ip a
ip addr
ip addr show
	     
# mostrar interfaces de red ip v6
ip -6 a
	     
#mostrar tabla de rutas, ouertas de enlace
route -n
	     
#nombre del host
hostname

# terminales en linux se representan por como tty
chvt # change foreground virtual terminal (cambia el tty de trabajo, puede ser un numero del 1 al 12, 7 reservado GUI)
chvt 3 # conectarse al terminal 3

# muestra la terminal actual en uso (ubicacion del archivo tty)
tty # /dev/pts/{nro} aqui se guardan la terminal virtual usada por el usuario
	     
# lista usuarios del sistema
sudo cat /etc/passwd | cut -d: -f1

# mostrar los usuarios conectados usando terminales vituales
w # mas detallado
# o
who # mas resumido

# imprimir el usuario de la sesion actual del shell
whoami
	     
# mostrar usuarios conectados 
ps -ft tty1

# matar a los procesos de usuario 
kill -KILL {PID}
kill -SIGKILL {PID}

# para visualizar la ip de un dominio
nslookup google.com
	     
# conexiones activas	     
netstat -ltn

# realizar consultas al dns
dig www.google.com

# check servidor DNS
grep "nameserver" /etc/resolv.conf

# programa para configurar dns
sudo apt install -y bind9
	     
### FIREWALL ###
sudo ufw (enable, reset, status) #: activar, desactivar o ver el estado y reglas de nuestro firewall.
sudo ufw allow numero-puerto#: permitir el acceso por medio de un puerto específico. Recuerda que el puerto 22 es por donde trabajamos con SSH.
sudo ufw status numbered#: ver el número de nuestras reglas.
sudo ufw delete numero-regla#: borrar alguna de nuestras reglas.
sudo ufw allow from numero-ip proto tcp to any port numero-puerto#: restringir el acceso de un servicio por alguno de sus puertos a solo un número limitado de IPs específicas.
### LO MISMO PERO DICHO DE OTRA FORMA ###
sudo ufw status#: Muestra el estado (activo/inactivo) y las reglas del firewall. Con el modificador numbered me muestra las reglas numeradas
sudo ufw allow puerto#: Habilita un puerto
sudo ufw enable#: Enciende el firewall
sudo ufw delete numero_de_regla#: Borra una regla
sudo ufw allow from direccion_ip proto protocolo to any port puerto#: Restringe las direcciones ip que pueden conectarse a cierto puerto. Recordar que SSH trabaja con el protocolo TCP
sudo ufw reset#: Elimina todas las reglas

	     
# escaneo simple de vulnerabilidades del host
sudo apt install lynis	     
sudo lynis audit system > reporte.txt
	     
CONFIGURACION TARJETA RED-
#ifconfig = comando para obtener informacion sobre la red (direccion ip,mascara,direccion mac etc)
#system-config-network-tui = interfaz grafica de red 
#/etc/init.d/network restart = reinicio de interfaces de red


#Procesos mas CPU consumen en el S.O.
sudo ps auxf | sort -nr -k 3 | head -5

#Procesos mas RAM consumen en el S.O.
sudo ps auxf | sort -nr -k 4 | head -5  

	     
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

# listar todos los servicios
service --status-all
# listar todos los servicios corriendo
service --status-all | grep +


	     
	     
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





# GRUPOS
groupadd #= Creación de grupos 
groupmod #= Modificación de grupos 
groupdel #= Eliminación de grupos 
	     
# crea un usuario sin asignarle contraseña, se debe configurar a mano posteriormente.
useradd {usuario}
	
# crear un usuario asignando contraseña y datos personales
adduser {usuario}

# borrar un usuario
userdel {usuario}
	     
# modifica de usuario
usermod {usuario}

# suplantar a un usuario
su - {usuario}

# mostrar permisos del usuario actual
sudo -l

# mostrar grupos a los que pertenece un usuario
groups {usuario}

# agrega un usuario a un grupo
gpasswd -a {usuario} {grupo}

# quita a un usuario de un grupo
gpasswd -d {usuario} {grupo}

# agrega un usuario a un grupo
usermod -aG {grupo} {usuario}

# evalúa si una contraseña es buena o mala del 0 al 100
pwscore





cat /usr/sbin/nombre_de_comando # muestra el contenido de un comando

# crear un usuario especificando contraseña y datos 
id 				# nos muestra el identificador único (uid) de cada usuario  
id {usuario} 			# detalles sobre el usuario
groups {usuario} 		# La orden groups muestra la pertenencia al grupo
gpasswd -a {usuario} {grupo} 	# Puede agregar un usuario a un grupo 
gpasswd -d [usuario] [grupo] 	# Puede eliminar un usuario de un grupo
passwd {nombredeusuario} 	# Para especificar la contraseña del usuario
chage -l {nombredeusuario}  	# Checkear expiracion de la password del usuario
passwd -x -1 {nombredeusuario}	# Setear que nunca expire la contraseña usando binario passwd
chage -M -1 {nombredeusuario}	# Setear que nunca expire la contraseña usando binario chage


cat /etc/shadow		#= Información reservada de las cuentas de usuario, password encriptadas
cat /etc/passwd		#= Información de las cuentas de usuario
cat /etc/gshadow	#= Contiene información reservada de los grupos de usuarios
cat /etc/group	 	#= Define a que grupos pertenecen los usuarios
cat /etc/sudoers	#= Lista lo que se puede ejecutar con sudo
cat /home/*	 	#= Carpeta personal del usuario

su usuario 	#= permite cambiar el usuario
su 		#= cambia por usuario root
newgrp {grupo}  #= permite cambiar el grupo primario del usuario actual


------------PROPIEDADES ARCHIVOS Y PERMISOS
lectura (r), escritura (w) y ejecución (x)
(r) tiene 4, 
(w) tiene 2, 
(x) tiene 1. 
 
chmod 777 archivo 		#= cambia permisos de archivo, da todos los permisos a todos los usuarios (mala practica)
chgrp gruponuevo archivo 	#= cambia de grupo propietario el archivo
chown usuario archivo 		#= cambia usuario propietario del archivo

chmod = lo puede usar: root y el propietario del archivo
u = user
g = group
o = others
a = all

chmod u+x archivo.txt # dar pemiso al usuario de ejecucion del archivo de texto
chmod g-w archivo.txt # quitar permiso al grupo de escritura del archivo de texto
chmod +x codigo.sh # dar permiso de ejecucion a todos (usuario, grupo y otros) de la shell codigo.sh


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

# Lista los servicios del sistema
sudo systemctl list-units -t service --all
	     
# Muestra el log de un servicio
sudo journalctl -fu servicio
	     
	     
# Muestra cuanto pesan los logs en el sistema operativo
sudo journalctl --disk-usage
	   
# Muestra los booteos de la computadora  
sudo journalctl --list-boots
	     
# Muestra mensajes de determinada categoría de nuestros logs
sudo journalctl -p critic|notice|info|warning|error
	
# Muestra los logs en formato json     
sudo journalctl -o json


		
# Ver cuanto pesa un archivo en MB
du -h nombre_archivo

# Ver cuanto disco utilizan en el directorio /var ordenado por peso y mostrando el top 5 de los resultados
du -h /var/ | sort -rh | head -5

# Desplegar programas instalados en linux
dpkg-query -l

# Desplegar programas instalados en linux, solo los nombres, sin mostrar la version ni descripcion
dpkg-query -f '${binary:Package}\n' -W

# Buscar en el cache de apt programas que calcen con python3-pip
apt-cache search python3-pip


# Red Hat / CentOS / Fedora
# .rpm Red Hat Package Manager.

# ver el contenido de la dase de datos RPM
cat /var/lib/rpm

# Listar todos los rpms instalados en la máquina. (query all)
rpm -qa

# Realizar la instalación de un paquete. (install)
rpm -i {paquete}.rpm

# Remover un paquete del sistema. (erase)
rpm -e {paquete}.rpm

# Repositorios yum Permite instalar un paquete desde un repositorio sin tener que conocer la ruta del archivo o las dependencias.
yum install {paquete}

# Muestra la información de un paquete
rpm -qi {paquete}

# Muestra los archivos asociados a un paquete
rpm -qc {paquete}


# Debian / Ubuntu
# .deb Debian package management.
# ver el contenido de la base de datos DPKG
cat /var/lib/dpkg

# Listar todos los debs instalados en la máquina.
dpkg -l

# Realizar la instalación de un paquete.
dpkg -i {paquete}.deb

# Remover un paquete del sistema.
dpkg -r {paquete}.deb

# Volver a ejecutar el asistente de configuración si está disponible.
dpkg-reconfigure {paquete}
	     
# repositorios apt otra forma de instalar.
apt install {paquete}




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


FECHA Y HORA DE LINUX Y LA BIOS
	     
# validar fecha y hora de linux
date

# validar fecha y hora de la BIOS
hwclock

# archivo de configuracion de la zona horaria de linux, se puede borrar para establecerla denuevo, archivo se crea automaticamente denuevo si se borra
cat /etc/adjtime

# Ejemplo para setear la fecha y hora de linux 27-Mayo-2007 y la hora 17:27
date --set "2007-05-27 17:27"

# Ejemplo para setear la fecha y hora de la BIOS 27-Mayo-2007 y la hora 17:27
hwclock --set --date="2007-05-27 17:27"

# para igualar ambas horas, la de linux con la BIOS
hwclock --set --date="`date '+%D %H:%M:%S'`"
# para sincronizar la hora, si la pila está agotada, para que setee la "hora buena" en cada reinicio 
# se puede editar el fichero /etc/rc.d/rc.local y colocar al final "ntpdate -u ntp.ubuntu.com"

# cambiar la zona horaria por link simbolico, ejemplo apuntando el archivo localtime a la zona horaria de chile continental que a su vez apunta a santiago/america
sudo ln -s /usr/share/zoneinfo/Chile/Continental /etc/localtime	     
	     
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


#Archivos .gz:
Comprimir: # gzip archivo.txt
Descomprimir: # gzip -d archivo.txt.gz
 

#Archivos .tar:
Empaquetar: # tar cf paquete.tar /carpeta/a/empaquetar/
Ver contenido del paquete: # tar tf paquete.tar
Empaquetar y ver contenido empaquetado: # tar -cvf paquete.tar /carpeta/a/empaquetar/
Desempaquetar: # tar xf paquete.tar
 

#Archivos .tar.gz:
Empaquetar y Comprimir: # tar czf empaquetado.tar.gz /carpeta/a/empaquetar/y/comprimir
Descomprimir: # tar xzf archivo.tar.gz



HARDWARE & SOFTWARE INFO

# validar memoria ram libre en servidor
free -h

# validar memoria ram inactiva, no asignada a ningun proceso
vmstat -s -S M
cat /proc/meminfo/

# validar utilizacion de los discos del servidor
df -h

# validar discos duros y particiones de un servidor
fdisk -l

# validar discos, particiones y volumenes logicos en el servidor
lsblk

	     
	     
lscpu
lshw
hwinfo
lspci
lsscsi 
lsusb
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


### OPEN SSL ###
# generar clave privada RSA con 2048 bits de largo
openssl genrsa -out private_key.pem 2048 # validacion 'cat private_key.pem'

# generar clave publica a partir de la llave privada recien creada
openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem # validacion 'cat public_key.pem'

# para realizar una prueba de encriptacion se creara un archivo de texto plano
echo 'This is a secret message, for authorized parties only' > secret.txt

# encriptacion del archivo de text secret con la llave publica (para que se pueda desencriptar con la llave privada)
# archivo de salida encriptado queda con nombre 'secret.enc'
openssl rsautl -encrypt -pubin -inkey public_key.pem -in secret.txt -out secret.enc

# desencriptar el archivo recien encriptado con la llave privada
openssl rsautl -decrypt -inkey private_key.pem -in secret.enc

# para crear un resumen de hash del mensaje y una firma digital, usando algoritmo SHA256, se firma con la llave privada 
# archivo de salida con la firma quedara con nombre 'secret.txt.sha256'
openssl dgst -sha256 -sign private_key.pem -out secret.txt.sha256 secret.txt

# verificacion con llave privada de que el archivo no se ha modificado desde que se creo y encripto 
openssl dgst -sha256 -verify public_key.pem -signature secret.txt.sha256 secret.txt

### MD5, SHA1 y SHA256 ###

# a modo de prueba se creara un archivo 
echo 'This is some text in a file, just so we have some data' > file.txt

# obtener un hash MD5 del archivo de texto 'file.txt' recien creado
md5sum file.txt > file.txt.md5 # validacion del archivo recien creado que contiene el hash MD5 'cat file.txt.md5'

# verificar que el hash sea correcto y que el archivo original no haya sido manipulado desde que se creó
md5sum -c file.txt.md5

# obtener un hash SHA1 del archivo de texto 'file.txt' recien creado
shasum file.txt > file.txt.sha1

# verificar que el hash SHA1 sea correcto y que el archivo original no haya sido manipulado desde que se creó
shasum -c file.txt.sha1

# obtener un hash SHA256 del archivo de texto 'file.txt' recien creado
shasum -a 256 file.txt > file.txt.sha256

# verificar que el hash SHA256 sea correcto y que el archivo original no haya sido manipulado desde que se creó
shasum -c file.txt.sha256



### TCPDUMP ###

# snifar todos los paquetes sin especificar una interfaz
sudo tcpdump

# chequear interfaces de red que se puedan snifar
ip link

# snifar los paquetes que pasen por la interfaz eth0
sudo tcpdump -i eth0

# snifar los paquetes que pasen por la interfaz eth0, activando el resultado detallado (-v) y no resolviendo los nombres de host ni los puertos (-n)
sudo tcpdump -i eth0 -vn

# lo mismo de arriba pero filtrando los paquetes, se capturaran solo los paquetes que vallan o provengan del host 8.8.8.8 y que usen el puerto 53 para comunicarse
sudo tcpdump -i eth0 -vn host 8.8.8.8 and port 53
# para probar comando anterior se puede usar el siguiente comando en otra terminal para generar trafico
dig @8.8.8.8 A example.com

# para guardar paquetes capturados a un archivo 
sudo tcpdump -i eth0 port 80 -w http.pcap
# para probar comando anterior se puede generar trafico HTTP en otra terminal con el siguiente comando
curl example.com

# para analizar el archivo http.pcap creado en el comando anterior
tcpdump -r http.pcap -nv










# TMUX
Send prefix CTRL + B

O - cambiar de panel en la ventana
! - cambiar panel actual a toda la ventana
" - dividir ventana actual y abrir otro panel
% - dividir ventana actual en dos horizontalmente
& - matar ventana actual
, - renombrar sesion actual
; - cambiar al ultimo panel
? - listar todos los atajos de teclado
C - crear nueva ventana
0 al 9 - mover entre ventanas
T - muestra la hora
W - seleccionar la ventana interactivamente
X - cerrar el panel avtual
CTRL + arriba/abajo/izq/der - reajustar tamaño de paneles




     
	     
BONUS:
	     
	     
# recatar archivos con foremost
foremost -v -t all -i /dev/sdb -o /home/shalo/recuperacion

# rescatar fotosd con foremost
foremost -T -t jpg -i /dev/sdb1

# recatar distintos tipos de archivos
foremost -T -va -t txt,jpg,wav,pdf,doc -i /dev/sd/image.dd -o /dev/sd

# archivo de configuracion de foremost
vim /etc/foremost.conf

# conexion a canal irc
irssi
	     /connect irc.freenode.com
	     /join #testchannel
	     






#################
### SCRIPTING ###
#################
Examples of cat <<EOF syntax usage in Bash:


1. Assign multi-line string to a shell variable

$ sql=$(cat <<EOF
SELECT foo, bar FROM db
WHERE foo='baz'
EOF
)

The $sql variable now holds the new-line characters too. You can verify with echo -e "$sql".








2. Pass multi-line string to a file in Bash

$ cat <<EOF > print.sh
#!/bin/bash
echo \$PWD
echo $PWD
EOF

The print.sh file now contains:

#!/bin/bash
echo $PWD
echo /home/user










3. Pass multi-line string to a pipe in Bash

$ cat <<EOF | grep 'b' | tee b.txt
foo
bar
baz
EOF

The b.txt file contains bar and baz lines. The same output is printed to stdout.
