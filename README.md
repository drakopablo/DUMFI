# DUMFI
Download UM Files Immediately --- @author: Pablo Guillén Marquina


	##################
	## Introducción ##
	##################

Este script se centra básicamente en descargar los *"Recursos"* de las asignaturas que estemos cursando (y por tanto matriculadas) de la forma más simple, fácil y rápida posible.

Para poder ejecutarlo, debemos introducir los siguientes datos en el script:

1. <u>Correo UMU del usuario</u>: ejemplo@um.es
2. <u>Contraseña del correo UMU</u>:  ejemplo01
3. <u>Carpeta de destino (donde queremos guardar los archivos)</u>: C:\User\Desktop\ejemploUMU
4. <u>Unidad de volumen disponible</u>: Z
  * Normalmente, suelen estar utilizados los volumenes "C:" y "D:", por lo que, por defecto, utilizamos el "Z:", o aquel que el usuario elija (y que esté disponible para el intercambio)
5. Lista de las asignaturas con sus códigos:
  * En ***batch*** esto <u>no</u> es posible, y debemos ejecutar los scripts de las asignturas uno a uno. Se puede simular el uso de listas usando la directiva *"setlocal EnableDelayedExpansion"*, - pero aún no he encontrado la manera de que funcione -.

  * En ***python*** esto sí es posible, por lo que usamos un diccionario que relacione estos datos.

    

 	#######################
 	## Args del programa ##
 	#######################
1. Ruta completa de la carpeta destino donde guardar los archivos descargados:
	"C:\Users\???\Documents\TestUM"

2. Código de la asignatura (matriculada, of course), de la que se quiere descargar el material de la carpeta recursos. Este se puede encontrar tanto en la URL del AV, como en el apartado "Recursos > Transferir archivos":
	"3890_G_2021_N_N"

3. Nombre de la unidad de volumen que se quiere utilizar para hacer la conexión con el AV:
	"Z" (por ejemplo)	--> 	"Z:\"
4. Usuario y contraseña del AV:
	"pepe@um.es"	"pepe01"


	##########
	## URLs ##
	##########
*URL:	(conectarse a una unidad de red en Win10)*
https://www.solvetic.com/tutoriales/article/2985-como-mapear-conectar-unidad-de-red-en-windows-10/

*URL:	(copiar varios archivos y carpetas en Win10)*
https://www.ubackup.com/backup-restore/xcopy-command-to-copy-folders-and-subfolders-6688.html

*URL:	(uso del comando "xcopy" en Win10)*
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy

*URL:	(truquillo para que xcopy no copie de más) **[desuso]***
https://stackoverflow.com/questions/17587347/batch-file-to-run-xcopy-without-overwriting-existing-files
	(*) Resumen: echo n|xcopy s:\* z:\ /E 

+ Aunque realmente no es necesario, así que se opta por usar la opción /Y de xcopy para que sobreescriba todo directamente, sin necesidad del mensaje de confirmación. 

*URL:	(crear listas en batch)*
https://stackoverflow.com/questions/10166386/arrays-linked-lists-and-other-data-structures-in-cmd-exe-batch-script/10167990#10167990




	#######
	## ? ##		// No hagas mucho caso
	#######

*Uso (?):*
[Código] (\\aulavirtual.um.es@SSL\DavWWWRoot\dav) [Unidad de red]

*Ejemplo: (Dsint 2021)*
3890_G_2021_N_N (\\aulavirtual.um.es@SSL\DavWWWRoot\dav) (Z:)

+ Para ejecutar un comando del sistema en C/C++:
  	#include <stdlib.h>

	int main() {
	    system("_comando_");
	    return 0;
	}

+ Opciones de xcopy:
  	/m/e/s/h/d/i/c/y




```
##########################
## Añadir unidad de red ##
##########################
```

*Uso:*
Net use [Vol_name:] \\aulavirtual.um.es@SSL\DavWWWRoot\dav\[Código_asignatura] /persistent:(yes/no) /user:user password

*Ejemplo:*
Net use Y: \\aulavirtual.um.es@SSL\DavWWWRoot\dav\3890_G_2021_N_N /persistent:yes /user:"pepe@um.es" pepe01




	##########################
	## Borrar unidad de red ##
	##########################
+ Para desconectar una unidad de red concreta o todas las redes mapeadas Windows 10, usa alguno de estos comandos:

  ​	net use [vol]: /delete 	# Borra una unidad de red concreta
  ​	net use * /delete  		  # Borra todas las unidades de red conectadas
  
  


	########################
	## A tener en cuenta: ##
	########################
+ Podemos poner una asignatura por unidad de red. Dependiendo de la opción de persistencia, las unidades de red se mantendrán o no al reiniciar el ordenador.

+ Si no hay ninguna unidad de red libre, produce error (no sé si hay limitación de nombres).

+ En el peor caso, si solo queda disponible una unidad de red, se usará esa conectando y desconectando la unidad sucesivamente tras haber actualizado el material descargado de las sucesivas carpetas "Recursos".

+ Por alguna razón que todavía no sé, la unidad de red sí que se conecta, pero no aparece en la carpeta de "Equipo". No sé si es porque permanece oculta o qué, pero no debería de hacer eso. Además, las unidades conectadas "manualmente" no se eliminan con el comando "\delete"

  


	##############################
	## Futuras actualizaciones: ##
	##############################

* **<u>PROGRAMAR LA TAREA</u>:**
  
  Existe una forma de hacerlo por comando y, para ello, sería interesante contar con la interfaz de usuario primero para que éste elija las opciones para que se cree/modifique la tarea más fácilmente:
  https://www.windowscentral.com/how-create-task-using-task-scheduler-command-prompt
  
  * De momento lo hacemos de forma manual:
  
    * Abrimos el panel de control:
  
      ![programar_la_tarea - panel de control](.\Programar tarea - manual\programar_la_tarea - panel de control.jpg)
  
    * Buscamos la opción para crear la tarea: **Herramientas administraticas > Programar tarea**
  
      ![programar_la_tarea - buscar schtask](C:\Users\Dragg\Desktop\Desktop\Projects\DUMFI\Programar tarea - manual\programar_la_tarea - buscar schtask.jpg)
  
    * Seleccionamos la opción de **"Crear tarea..."** en el menú que vemos a la derecha:
  
      ![programar_la_tarea - programador de tareas](C:\Users\Dragg\Desktop\Desktop\Projects\DUMFI\Programar tarea - manual\programar_la_tarea - programador de tareas.jpg)
  
    * Creamos la tarea con la información **<u>General</u>**:
  
      ![programar_la_tarea - creacion tarea](C:\Users\Dragg\Desktop\Desktop\Projects\DUMFI\Programar tarea - manual\programar_la_tarea - creacion tarea.jpg)
  
    * Escogemos las **<u>Condiciones</u>** para la ejecución de la tarea:
  
      ![programar_la_tarea - condiciones](C:\Users\Dragg\Desktop\Desktop\Projects\DUMFI\Programar tarea - manual\programar_la_tarea - condiciones.jpg)
  
    * Elegimos la **<u>Acción</u>** que queremos que realice. En nuestro caso, que ejecute el script *"dumfi.py"*:
  
      ![programar_la_tarea - ejecutar accion](C:\Users\Dragg\Desktop\Desktop\Projects\DUMFI\Programar tarea - manual\programar_la_tarea - ejecutar accion.jpg)
  
    * Seleccionamos los *"triggers"* o **<u>Desencadenantes</u>** que haran que nuestra tarea se ejecute periódicamente:
  
      ![programar_la_tarea - triggers](C:\Users\Dragg\Desktop\Desktop\Projects\DUMFI\Programar tarea - manual\programar_la_tarea - triggers.jpg)
  
    * Le damos a **"Aceptar"**,  ¡y ya estaría creada nuestra tarea!
  
    * Inicialmente, aunque le demos a "Actualizar" en el "Programador de Tareas", no nos aparecerá la tarea. Esto es normal. Para comprobar que la tarea está bien creada, podemos comprobarlo a través de un sencillo comando de bash en **cmd**: *"schtasks | more"*
  
      
  
* **<u>A TRAVÉS DE LINEA DE COMANDOS</u>:**

  * Crear un comando en bash (por ejemplo: ***"dumfi --update"***), que actualice todas las asignaturas.
  
    
  
* **<u>SUSCRIPCIONES</u>:**

  * Esto se refiere a que un alumno se "suscriba" a una asignatura. De esta forma, se sabe el nombre y el código de la asignatura suscrita y, siempre y cuando el alumno tenga acceso a ella (estando matriculado en ella), puede acceder a toda la información disponible. Esto es:
    * Descargar "Recursos" virtuales de la carpeta de la asignatura.
    * Acceder al correo para comprobar, notificar y añadir al calendario, los aspectos importantes de la asignatura. Por ejemplo: **Al abrirse una tarea, se añade en el calendario la fecha de inicio y fin de la misma**; Cuando el profesor responde a un correo, se puede notificar al usuario (aunque de esto ya se encarga el AV).

  

* **<u>AMPLIAR A TODA LA UMU</u>:**

  * Esto se refiere a mediante el uso de una **Base de datos no relacional** (nosql, por ejemplo), poder listar la información de todos los grados y todas las asignaturas de los grados. De esta forma, si una persona hace más de una carrera a la vez, puede acceder a esas asignaturas de una forma más visual y rápida.
  * Para esto, se usará un interprete de datos en Python para leer la información de los ficheros JSON. De forma que se pueda acceder de forma inmediata a los datos de "las tablas".

s

s
