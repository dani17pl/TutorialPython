'''
Created on 16 sept. 2018

@author: Dani_
'''

#Informacion: https://docs.python.org/3.7/library/stdtypes.html#string-methods.
if __name__ == '__main__':
#Métodos de búsqueda
    s='abrakdabra'
    #str.find(sub[, start[, end]]): devuelve la posición menor en la que se localiza la subcadena sub
    print(s.find('a',1,5))
    #str.rfind(sub[, start[, end]]): realiza la misma operación que find pero devuelve la posición mayor
    print(s.rfind('a'))
    #str.count(sub[, start[, end]]): cuenta el número de ocurrencias de la subcadena
    print(s.count('a',1))
    #str.startswith(prefix[, start[, end]]): devuelve True si la cadena str comienza con el prefijo prefix
    print(s.startswith('a'))
    #str.endswith(suffix[, start[, end]]): es similar al método anterior, pero sirve para realizar comprobaciones con sufijos
    print(s.endswith('a'))
#Metodos de sustitucion
    #str.replace(old, new[, count]): devuelve una nueva cadena en la que las ocurrencias de la subcadena old en str se sustituyen por la subcadena new.
    print(s.replace('a','o'))
    #str.strip([chars]): devuelve una nueva cadena en la que se eliminan los caracteres del comienzo y final de str que coincidan con los contenidos en la cadena chars.
    print(s.strip('a'))
    #str.lstrip([chars]): es una versión del método anterior en la que sólo se eliminan caracteres del comienzo.
    print(s.lstrip('a'))
    #str.rstrip([chars]): es una versión del método strip() en la que sólo se eliminan caracteres del final.
    print(s.rstrip('a'))
#Metodos de Fragmentacion
    #str.split(sep=None, maxsplit=-1): devuelve una lista1 de subcadenas que resultan de fragmentar la cadena str usando la subcadena sep como separador. Si no se especifica sep, la separación se realiza en los espacios en blanco.
    print(s.split('b'))
    #str.splitlines([keepends]): realiza la misma operación que el método anterior, pero la fragmentación se realiza en los saltos de línea. Si se especifica keepends y su valor es True, entonces los saltos de línea se conservan en las subcadenas fragmentadas.
    
#Formateo de cadenas
    #cadena_de_formato % (arg1,...,argn)  Como printf en C
    n = 2 
    s = 'Hay %d maneras de %s una cadena en Python' % (n,'formatear')
    print(s)
    x = 1.23456789 
    s = ' %-6.2f | %05.2f | %+06.1f' % (x, x, x)
    print(s) # Imprime ’1.23 | 01.23 | +001.2’
    
    plantilla = '{0}, {1} y {2}' 
    s = plantilla.format('spam', 'jamón', 'huevos')
    print(s) # Imprime ’spam, jamón y huevos’