'''
Created on 16 sept. 2018

@author: Dani_
'''
import prog1 # Importamos todas las definiciones de b.py
#import dijkstra as d # d.x para acceder al identificador x de dijsktra (indicar nombre distinto)
from prog1 import *
#Si fuesen varias las definiciones importadas, se indicarían separadas por comas. Si se quieren importar todas, se usa un asterisco *. 

if __name__ == '__main__':
    x=2 #No cambia x en prog 1
    print('x =',x) #imprime 2
    spam('zarangollo') #importcion 2 imprime spam 10 veces
    
    prog1.x=2 #cambia x en prog 1
    print('x =',x) #imprime 2
    spam('zarangollo') #importcion 2 imprime spam 2 veces
    
    