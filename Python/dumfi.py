"""
*---------- DUMFI v0.1 -----------*
** Download UM Files Immediately **
***********************************
Created on Mon Sep 20 23:00:49 2021

@author: Pablo Guillén Marquina
"""

import os      # system()
import time    # sleep()

class dumfi:
    '''
        Debemos crear una instancia de esta clase con los parámetros necesarios
    '''
    def __init__(self, user, pasw, dest, vol, subjects): 
        '''
        TODO: Mejoras pendientes de implementar:
            1. Opción de ver las asignaturas
            2. Opción de añadir/modificar/eliminar asignaturas
            3. Opción de organizar las asignaturas por cuatrimestre/curso/año
            4. Opción de crear un perfil para guardar las credenciales (?)
            5. Interfaz de Python para elegir las preferencias de usuario
            6. Sistema de leer/escribir la información del usuario para que solo deba introducir los datos la primera vez
            7. Usar comando "schtask" para crear una tarea que ejecute el script periodicamente (Windows 10)
            
        [!] Hay que tener en cuenta que no reconoce todos los caracteres en las rutas (p.e.: al usar "." en el nombre de una carpeta)
        '''
        # Variables que no se cambian
        self.url = "\\\\aulavirtual.um.es@SSL\\DavWWWRoot\\dav\\"
        self.sufix =  "_G_2021_N_N"
        # Variables que se pueden cambiar
        self.vol = vol
        self.opts = f"/m/e/s/h/d/i/c/y"
        # Variables que se deben cambiar (ya sea por comando o a mano)
            # Carpeta destino de los archivos/subcarpetas
        self.dest = dest
            # Credenciales
        self.user = user
        self.pasw = pasw
             # Asignaturas con sus códigos
        self.subjects = subjects
        
        # Mensajes de aviso
        self.msg1 = "ECHO La unidad seleccionada \"%s:/\" se usará para conectarse en red a la url \"%s%s\" y los archivos serán descargados dentro de la carpeta \"%s\"." % (self.vol, self.url, "\"Código_Asignatura\""+self.sufix, self.dest)
        self.msg2 = "ECHO Por favor, verifique que los datos anteriores son correctos antes de continuar. Si no lo son, habrá el script y cambielos manualmente."
        
        # Iniciamos
        self.start()
      
        
    def start(self):
        '''
            Método que se ejecuta al crear la clase.
            TODO: aquí se podrían leer los datos de un fichero aparte para que el siguiente mensaje tenga sentido.
        '''
        os.system(f"ECHO ¡Bienvenido {self.user}! Los datos del usuario han sido leídos correctamente.")
        
        # Ejecutamos el método principal
        self.main()


    def main(self):
        '''
            Método principal de la clase
        '''
        os.system(self.msg1)
        print("\n")
        os.system(self.msg2)
        print("\n")
        #os.system("PAUSE")
        for i in range(len(self.subjects)):
            subj = self.subjects[i+1][0]
            # OPIONAL: Para cada asignatura creamos una subcarpeta (opcional). Eliminamos el error producido por carpetas ya creadas
            os.system(f"MKDIR {self.dest}\{subj} 2> nul")
            # Por cada asignatura, descargamos el material actualizado en su carpeta correspondiente
            subj = subjects[i+1][0]
            code = subjects[i+1][1]
            print (subj, "-", str(code)+self.sufix, ":")
            # Añadimos la unidad de red: (Eliminamos el error que aparece cuando todavía no se ha terminado de desconectar el recurso de red)
            cmd1 = f"NET USE {self.vol}: {self.url}{code}{self.sufix} /persistent:no /user:{self.user} {self.pasw} 2>nul"
            os.system(cmd1)            
            # Copiamos los archivos a la carpeta destino:
            cmd2 = f"XCOPY {self.vol}:\. {self.dest}\{subj} {self.opts}"
            os.system(cmd2)
            # Borramos la unidad de red usada:
            cmd3 = f"NET USE {self.vol}: /delete /Y > nul"
            os.system(cmd3)
            print("\n")
            time.sleep(1)   # Esperamos un segundo
        
        # Finalizamos el programa
        print("\n")
        cmd = f"echo ¡Todas las asignaturas están actualizadas! ¡Adios, {self.user}!"
        os.system(cmd)


## Programa principal ##
if __name__=="__main__":
    # Información necesaria para crear la clase
        # Introducimos correo UM
    user = "ejemplo@um.es"
        # Introducimos contraseña
    pasw = "ejemplo"   
        # Elegimos la dirección destino
    dest = "C:\\Users\\???\\Desktop\\???"
        # Elegimos una unidad de volumen disponible
    vol = "Z"
    
    # Creamos un diccionario que relaciona las asignaturas del curso con sus códigos 
    subjects = {
        1 : ["DSINT", 3890],
        2 : ["PIA", 1923],
        3 : ["AC", 3891],
        4 : ["FCV", 3861],
        5 : ["CMULT", 1919]
    }
    
    # Creamos la clase (y se ejecuta)
    phil = dumfi(user, pasw, dest, vol, subjects)
    os.system("exit")