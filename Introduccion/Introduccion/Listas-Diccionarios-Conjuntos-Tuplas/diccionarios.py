'''
Created on 16 sept. 2018

@author: Dani_
'''
#Un diccionario es una colección no ordenada – y, por tanto, no secuencial – de valores que se almacenan y 
#recuperan mediante una clave en lugar de usar una posición
if __name__ == '__main__':
#Operaciones Basicas
    X = {} # Diccionario vacío
    D = { 'nombre':'Santiago Paredes', 'alias':'Chapu', 'dpto':'DIIC' }
    print(D)
    #los valores, no tienen ninguna limitación y, por ejemplo, podríamos encontrar diccionarios o listas dentro de diccionarios.
    #segunda forma de crear diccionarios es mediante el método dict(), con dos variantes: 
        #especificando una lista de pares (nombre,valor)  
    D = dict([('nombre','Santiago Paredes'),('alias','Chapu'),('dpto','DIIC')])  
        #bien una lista de argumentos nombrados:
    D = dict(nombre='Santiago Paredes', alias='Chapu', dpto='DIIC')
    
    #Consulta
    print(' %s es del departamento %s' % (D['alias'],D['dpto']))
        #Si la clave no existe en el diccionario, se lanza una excepción KeyError. Por tanto, puede resultar útil verificar si un diccionario contiene una entrada con una determinada clave
    if 'alias' in D:
        print(D['alias'])
        #a alternativa con el método get() para recuperar un valor a partir de su clave,no se lanza la excepción KeyError sino que se devuelve el valor None:
    D = { 'uk':'Turing', 'eeuu':'Church', 'cz':'Gödel', 'de':'Hilbert'} 
    x = D.get('es')
    print(x) # Imprime None
    x = D.get('es','Manolete')#segundo parámetro del método get() a modo de valor por defecto que se devuelve en caso de que no se encuentre la clave
    print(x) # Imprime ’Manolete’
    
    #dos métodos de los diccionarios que devuelven conjuntos para ser usados en la sentencia for-in.  keys(), y values(), 
    for k in D.keys(): 
        print('La clave %s tiene valor %s' % (k,D[k]))
        
    #Podemos realizar una copia de un diccionario usando el metodo copy().

#Modificación directa
    D = {} 
    D['nombre'] = 'Eduardo Martínez' # Añade una entrada
    D['nombre'] = 'Pepe Juárez' # Modifica el valor de una entrada
    del D['nombre'] # Y la elimina #Si la clave usada en la eliminación no existe, se lanza la excepción KeyError.
    
    #Metodos
    D = { 'nombre':'Santiago Paredes','nombre':'daniel', 'nombre':'Daniel'} #Solo se guarda Daniel
    C={'nombre':'Sonia','alias':'hermana'}
    #D.pop(clave,defecto?): extrae y elimina una entrada con la clave indicada como primer parámetro.
    print(D) 
    x=D.pop('nombre')
    print(x) #Devuelve daniel
    print(D) #vacia
    #D.update(D2): inserta en el diccionario D todas las entradas del diccionario D2. En caso de que haya alguna clave en D2 que ya esté en D, se modifica su valor con
    D.update(C)
    print(D) #nombre Sonia
    D.clear()#elimina todas las entradas
    
    #Ejercicio 3(1 diccionarios)
    
    
    