'''
Created on 7 dic. 2018

@author: Dani_
'''
from jflap.Afd import Afd
import sys
from sys import stderr
import time

if __name__ == '__main__':
    repetir = True
    ruta = r'..\TorreHanoi.jff'
    try:
        automata = Afd(ruta)
    except FileNotFoundError:
        print('Me temo que la ruta está mal',file=stderr)
    except Exception as error:
        print('Problema analizando el fichero:',error,file=stderr)
      
                
    while (repetir):
        repetir = False
        nombreFichero = input('Introduce el nombre del fichero:')
        if (len(nombreFichero)==0):
            print('Has salido del programa')  
            sys.exit()        
        else:
            ruta = '..\\'+nombreFichero + '.txt'
            try:
                f = open(ruta)
            except FileNotFoundError:
                print('Me temo que la ruta está mal',file=stderr)
                time.sleep( 1 )
                repetir = True
            except Exception as error:
                print('Problema analizando el fichero:',error,file=stderr)
                time.sleep( 1 )
                repetir = True
        # Depuramos
    numLinea = 0
    for linea in f:
        estadoActual = automata.getEstadoInicial()
        numLinea = numLinea +1
        pos = 0
        linea = linea.strip('\n')
        lineaAimprimir = linea
        for i in linea:
            pos = pos + 1
            estadoActual = automata.estadoSiguiente(estadoActual,i)
            if (estadoActual=='q27'):
                    break;
        if(numLinea!=0):
            
            if (automata.esFinal(estadoActual)):
                print('Linea ' + str(numLinea)+ ': ' + lineaAimprimir + ': Valida')
            else:
                print('Linea ' + str(numLinea)+ ': ' + lineaAimprimir + ':No valida en '+ str(pos))

    
            
            
    
       