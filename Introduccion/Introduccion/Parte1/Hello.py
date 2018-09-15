'''
Created on 14 sept. 2018

@author: Dani_
'''
def f(a,b,c=0): 
    return a+b*c
#la variable __name__ toma como valor el nombre del módulo 
#importado, de forma que no se ejecuta nada en este caso.
if __name__ == '__main__':
    #uso de 3 ' para que se tomen los saltos de lines en el mismo print
    print('''Ahora empezamos por aquí y
continuamos hasta aquí''')
    #cadenas raw. El carácter de contrabarra \ se deja intacto en la cadena.
    print(r'\d\t\d\n')
    
#Tipos
    #Conversion de tipos
    x = int("123") # Convierte una cadena en entero corto 
    y = float("1.2e-3") # Convierte una cadena en real
    z = complex("1+2j") # Convierte una cadena en complejo  
    #verificar tipo
    print(type(z)) # Indica <class ’complex’>
    #Comprobacion de tipos
    print(isinstance(y,int))
    
#variables
    #las variables no tienen que ser declaradas antes de su uso
    #posibilidad de dar distinto valor a las variables
    a = 23.5 
    print(a)
    a = "Y ahora soy una ’cadena de caracteres’" 
    print(a)
    
#Operadores
    #Operador aritmético Descripción 
        #x + y (suma)
        #x − y (resta)
        #x ∗ y (multiplicacion)
        #x / y (division)
        #x // y (division entera)
        #x%y (modulo)
        #+x −x (mas/menos unitario)
        #x ∗∗ y (potenci)

    #Operadores relacionales
        #las comparaciones de números reales pueden dar lugar a resultados inesperados
    x = 1.1 + 2.2
    print(x == 3.3) # Imprime False porque x contiene 3.3000000000000003
        #solucion:hacer una comprobación de lo próximos que se encuentran los dos números
    tolerancia = 1e-10 
    print(abs(x - 3.3) < tolerancia) # Imprime True
    
    #Operadores logicos
        #x or y Disyunción
        #x and y Conjunción 
        #not x Negación
    
    a = 0 
    b = 1 
    c = 2
    print(b and c) # 2 
    print(a and c) # 0
    
    x = ""  
    y = x or "valor por defecto" 
    print(y)
    
#Estructuras de control

    #Sentencia if
    print('{}, {}, {}'.format(a,b,c))
    if (a>b):
        print ('es',a)
    elif(a+1==b):
        print(f'es {a} y {b}')
    else:
        print('es',b, sep=':') 
    
    #Sentencia While
    i=0
        #While
    while (i<=3):
        print (i)
        i+=1
        
        #do while
    i=0
    while True:
        print (i)
        i+=1
        if not (i<=3):
            break
    
    #Sentencia For
    for x in [5,'7',11,'1bc',2]: 
        print(x,'es un número primo')
    
    a = 0
    for c in 'casa': 
        print(a,c)
        a += 1
    #range(start,stop,step)
    for c in range(0,-10,-2):
        print('c=',c)

#funciones (Mirar linea 6 declracion de funciones)
    print(f(1,2)) # El resultado es 3 
    print(f(1,2,3)) # El resultado es 6
    #
    print(f(c=2,a=1,b=3)) # El resultado es 5
            