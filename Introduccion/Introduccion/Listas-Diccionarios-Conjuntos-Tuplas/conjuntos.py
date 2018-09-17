'''
Created on 17 sept. 2018

@author: Dani_
'''
#Python ofrece un tipo de dato mutable conjunto, que únicamente tiene una restricción: sólo puede contener valores inmutables. 
if __name__ == '__main__':
#Operciones basicas
    alfabeto1 = { 'a','b','c','d' } 
    alfabeto2 = set(['0','1'])
    #añadir elementos al conjunto con el método add(), y eliminarlos con discard() o remove(). 
    print(alfabeto1) #Se imprimen en orden aleatorio
    alfabeto1.add('e')
    print(alfabeto1)
    alfabeto1.discard('b')
    alfabeto1.remove('c')
    print(alfabeto1)
    #método clear() es posible vaciar completamente un conjunto
    #pertenencia de un elemento a un conjunto
    if 'a' in alfabeto1: 
        print('a está en alfabeto1')
    #convertir un conjunto en una lista usando el método list()
    l = list(alfabeto1)

#Operaciones de conjuntos
    #operador de unión es |, el de intersección es & y el de diferencia es -
    #es ˆ, que permite hacer la diferencia simétrica de conjuntos (elementos que están en los conjuntos operados, salvo los que están en su intersección).
    #El operador >= equivale a la comprobación de conjuntos ⊇, mientras que > equivale a ⊃. 
    #Los operadores relacionales en sentido contrario <= y < tienen su correspondiente interpretación ⊆ y ⊂.
    A = { 'violín', 'viola', 'violonchelo' }
    B = { 'trompeta', 'trombón', 'trompa' } 
    C = { 'corneta', 'chirimía', 'sacabuche', 'bajón' }
    E = { 'viola' }
    D = A | B | C   #union
    print(D)
    D = A & E #interseccion
    print(D)
    D = A - E #diferencia
    print(D)
    D = A ^ E #diferencia simetrica
    print(D)
    if (E<=A):
        print('E esta incluido en A') #
    print(A>=E)