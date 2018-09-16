'''
Created on 16 sept. 2018

@author: Dani_
'''
#pueden contener instancias de cualquier tipo de dato, incluidas otras listas, y 
#son mutables, es decir, podemos modificar cualquier posición de una lista
if __name__ == '__main__':
#Operaciones basicas
    lista_vacía = []
    lista_no_vacía = [123, 'abc', 1.23, [1,2,3]]
    
    print(len([1,2,3]))
    l = [1,2,3]+[4,5,6] # Se genera la lista [1,2,3,4,5,6]
    l = [1]*10 # Se genera la lista [1,1,1,1,1,1,1,1,1,1]
    
    s = str([1,2,3]) # Genera la cadena ’[1,2,3]’
    l = list('123') # Genera la lista [1,2,3]
    
    l = [1,2,3]
    print(3 in l) # Imprime True 
    for x in l:
        print('Contiene',x)
    
    l = ['um','Um','UM'] 
    print(l[2]) # Imprime ’UM’
    x = l[:2] # Extrae [’Um’,’UM’]
    print(x)
    
    m = [[1,2,3],[4,5,6],[7,8,9]]   #Matriz
    print(m[1])
    print(m[1][1])
    
#Modificacion de listas
    #Modificación con indexación o troceado
    c = ['zarangollo','spam','spam','paparajote'] 
    c[1] = 'caldero'
    c[1:3] = ['pisto','marinera']
    print(c)

    c[1:3] = [] # Elimina posiciones 1 y 2
    del c[1] # Elimina la posición 1
    del c[1:3] # Elimina las posiciones 1 y 2
    print(c)
    
    d = ['zarangollo','paparajote']
    c[len(c):]=d #insertar elementos a una lista (le asignamos otra lista)
    print(c)
    
    #Modificación con métodos
    c = ['zarangollo','spam','spam','paparajote']
        #L.insert(i,X): inserta el valor X en la posición i de la lista.
    c.insert(1,'co')
    print(c)
        #L.append(X): añade el valor X al final de la lista.
    c.append('final')
    print(c)
        #L.extend(L2): añade la lista de valores L2 al final de la lista.
    d = ['zarangollo','paparajote']
    c.extend(d)
    print(c)
        #L.pop(i): elimina el valor que ocupa la posición i, y lo devuelve. Si no se indica el índice i, extrae el último elemento.
    print(c.pop(1))
    print(c)
        #L.remove(X): elimina la primera ocurrencia del valor X en la lista. Atención, lanza una excepción ValueError si la lista no contiene el valor X.
    c.remove('spam')
    print(c)
        #L.clear(): elimina todos los elementos de la lista.
    c.clear()
    print(c)
    
#Otras operciones
    c = ['zarangollo','spam','spam','paparajote']
    #L.index(X): devuelve la primera posición de la lista en la que aparece X; lanza ValueError si X no se encuentra en la lista.
    x=c.index('spam')
    print(x)
    #L.count(X): devuelve la cantidad de veces que aparece X en la lista.
    x=c.count('spam')
    print(x)
    #L.reverse(): invierte la lista.
    c.reverse()
    print(c)
    #L.copy(): genera una nueva lista que es copia de L.
    x=c.copy()
    print(x)
    #L.sort(). Por defecto, este método ordena en orden ascendente 
    c.sort()
    print(c)
    #l.sort(reverse=True) # ordena en orden descendente
    c.sort(reverse=True)
    print(c)