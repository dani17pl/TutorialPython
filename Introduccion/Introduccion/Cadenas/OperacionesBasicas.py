'''
Created on 16 sept. 2018

@author: Dani_
'''

if __name__ == '__main__':
#Concatenacion
    s = 'abc' + 'def' # forma la cadena ’abcdef’
    print(s)
#Repeticion
    s = 'Spam'*4 # repite 4 veces la cadena ’Spam’
    print(s)
#longitu
    s = 'abc' 
    print(len(s)) # imprime 3
#Indexcion
    s = 'spam'
    print(s[0],s[3])
    print(s[-1],s[-2],s[-3],s[-4]) #maps
#troceado
    s = 'spam'
    s = 'S'+s[1:4] # genera ’Spam’
    print(s)
    #extendida utiliza la sintaxis S[i:j:k], donde i y j tienen la misma interpretación que en la versión básica, y k indica el paso entre los elementos extraídos
    s = 'abcdefghijklmnop'
    print(s[1:10:2]) # imprime ’bdfhj’
#Conversion a cadena
    s = 'abc' + str(5) # forma la cadena ’abc5’ 
    print(s)
#Conversiones de caracteres
    c = ord('ñ')
    print(c) # imprime 241 
    s = chr(c)
    print(s) # imprime ñ
#Iteraccion con cadenas
    a = 0
    for c in 'super': 
        print(a,c)
        a += 1
#Comprobación de subcadena
    sub = 'fragil'
    if sub in 'supercalifragilisticoespialidoso':
        print('La contiene')