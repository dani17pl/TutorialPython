'''
Created on 2 oct. 2018

@author: Dani_
'''
from figuras2D import Rectangulo

if __name__ == '__main__':
    r1 = Rectangulo(5,4) # Crea un rectángulo con alto=5 y ancho=4 
    r2 = Rectangulo(8.3,20.1)
    print('Area de r1:',r1.área()) 
    print('Area de r2:',r2.área())