import sys

#El intérprete de Python coloca los argumentos con los que se ha invocado a la aplicación en la lista sys.argv.
if __name__ == '__main__':
#Argumentos del programa
    #o, si la aplicación está implementada en un módulo llamado a.py y recibe tres argumentos, se podría lanzar así:
    #$python a.py arg1 arg2 arg3
    #indicar los argumentos propiedadas  módulo a.py y editamos Run/Debug Settings
    if len(sys.argv) != 4:
        print('Uso: %s arg1 arg2 arg3' % (sys.argv[0]))
    else:
        #sys.argv[0] contiene el nombredel script.
        arg1 = sys.argv[1]
        arg2 = sys.argv[2] 
        arg3 = sys.argv[3]
    print (arg1, arg2, arg3)
    
#Entrada, salida y errores
    #Entrada estándar  función input()
    print("Indica tu sketch de los Monty Python favorito") 
    sketch = input("--> ")
    best = ['The Spanish Inquisition','Four Yorkshiremen','Brain Specialist'] 
    if sketch in best:
        print("¡Ése es genial!") 
    else: print("No está mal")
    
    #Salida estándar y salida de errores
        #Podemos modificar el separador usando el argumento nombrado sep:
    print('Uno',2,['a','b','3'],sep='.+.')
        #egundo argumento adicional del método print() es file, que permite especificar el flujoa través del cual se 
        #va a generar la salida. Por defecto (sys.stdout), pero podemos usarlo para producir mensajes de error a través de sys.stderr:
    print('¡Catástrofe: excepción capturada!',file=sys.stderr)
    
        #método end. Por defecto, print genera un salto de línea como último caracter de la cadena que se imprime. Podemos modificar este comportamiento
    print('No imprimas un salto ',end='') 
    print('porque quiero seguir en la misma línea')