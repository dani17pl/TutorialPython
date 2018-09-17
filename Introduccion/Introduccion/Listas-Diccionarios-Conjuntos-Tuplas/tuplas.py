'''
Created on 17 sept. 2018

@author: Dani_
'''
#Una tupla es como una lista inmutable, es decir, una secuencia ordenada que no puede cambiar.
# Se suele emplear para manejar colecciones de ítems que son fijas, como los meses de un año,
if __name__ == '__main__':
    N = ('do','re','mi','fa','sol','la','si')
    #N[0] = ’ut’ # Lanza una excepción TypeError
    #pueden crear tuplas usando la función tuple() que puede recibir como argumento una colección iterable (lista, conjunto u otra tupla).
    c = ['zarangollo','spam','spam','paparajote']
    print(c)
    E=tuple(c)
    print(E)