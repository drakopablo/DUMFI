@ECHO OFF
setlocal EnableDelayedExpansion

ECHO ¡Bienvenido a DUMFI! El gestor que no sabías que necesitabas y que la UMU no te ofrece.

REM ################# ESTO NO SE CAMBIA #####################
REM URL del aula virtual para conectarnos mediante unidad de red y el sufijo del código de la asignatura:
SET url=\\aulavirtual.um.es@SSL\DavWWWRoot\dav\
SET sufix=_G_2021_N_N
REM ##########################################################

REM ################## ESTO ES OPCIONAL ######################
REM Seleccionamos el volumen donde alojar nuestra unidad de red.
SET vol=Z
REM ##########################################################

REM ################# ESTO SÍ SE CAMBIA ######################
REM Seleccionamos la carpeta destino y (opcionalmente) creamos subcarpetas donde alojar nuestras asignaturas
SET dest=C:\Users\??\Documents\TestUM

REM Seleccionamos la asignatura que queremos descargar. En nuestro caso: DSINT
SET code=3890

REM Añanimos las credenciales para acceder al sitio web
SET user=ejemplo@um.es
SET pass=ejemplo
REM ##########################################################

REM ################## PROGRAMA PRINCIPAL ####################
ECHO La unidad seleccionada "%vol%:/" se usará para conectarse en red a la url "%url%%code%%sufix%" y los archivos serán descargados dentro de la carpeta "%dest%".

ECHO Por favor, verifique que los datos anteriores son correctos antes de continuar. Si no lo son, habrá el script y cambielos manualmente.
PAUSE

REM 'Añadimos la unidad de red
NET USE %vol%: %url%%code%%sufix% /persistent:no /user:%user% %pass%

REM 'Copiamos los archivos a la carpeta destino
SET opts=/m/e/s/h/d/i/c/y
XCOPY %vol%:\. %dest% %opts%

REM 'Borramos la unidad de red usada
NET USE %vol%: /Y
REM ##########################################################

PAUSE