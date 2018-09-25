'''
Created on 18 sept. 2018

@author: Dani_
'''

if __name__ == '__main__':
#abrir archivo
    archivo = open(r'C:\spam.txt')

#Lectura
    #Lectura completa
    contenido = archivo.read()
    print(contenido)
    #Lectura por líneas
    archivo = open(r'C:\spam.txt')    
    linea = archivo.readline()
    print(linea)
    
    archivo = open(r'C:\spam.txt')    
    lineas = archivo.readlines()
    n=1
    for linea in lineas:
        print('Linea %d: - %s-' % (n,linea.rstrip())) 
        n += 1
        
    #Lectura por caracteres o bytes
    tamaño_cabecera = 10 
    archivo = open(r'C:\spam.txt')   
    cabecera = archivo.read(tamaño_cabecera) 
    for b in cabecera:
        print(' %c' % (b), end=' ')

#Escritura
    archivo = open('salida.txt','w',encoding='latin1') 
    archivo.write('De minimis non curat praetor\n') 
    archivo.write('Aquila non capit muscas\n')
    archivo.write('Beati hispani quibus vivere bibere est\n')
    
    archivo = open('salida2.txt','w',encoding='latin1')
    latinajos = []
    latinajos += ['De minimis non curat praetor\n'] 
    latinajos += ['Aquila non capit muscas\n']
    latinajos += ['Beati hispani quibus vivere bibere est\n']
    archivo.writelines(latinajos)
    
#Otras funciones
    #orzar vaciado buffer sin cerrar el archivo, invocando al método flush():
    archivo.flush()
    
    #desplazamiento N desde el comienzo del fichero, podemos indicar la posición de la siguiente lectura o escritura usando seek():
    archivo.seek(N)
    
    #close
    archivo.close()
    