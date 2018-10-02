'''
Created on 2 oct. 2018

@author: Dani_
'''

class Rectangulo(object):
    '''
    classdocs
    '''
    #Variables de clase
    tipo = 'rectángulo' # Variable compartida por todas las instancias
    #El método inicializador siempre se llama igual en Python: __init(self,...)
    #self hace referencia a l instancia de la clase
    def __init__(self,alto,ancho): 
       self.alto = alto
       self.ancho = ancho
    #Definir metodos 
    def área(self): 
        return self.alto*self.ancho
        
#Herencia
class Punto3D:
    def __init__(self, x, y, z): 
        self.x, self.y, self.z = x, y, z
    def módulo(self):
        return (self.x**2+self.y**2+self.z**2)**0.5

class Punto2D(Punto3D):
    def __init__(self, x, y): 
        super().__init__(x, y, 0)

class Punto1D(Punto2D): 
    def __init__(self, x):
        super().__init__(x, 0)

if __name__ == '__main__': 
    p3 = Punto3D(4,2,2)
    p2 = Punto2D(3,4) 
    p1 = Punto1D(6)
    print(' %.2f %.2f %.2f' % (p3.módulo(),p2.módulo(),p1.módulo()))
    
    p1 = Punto3D(4,2,2) 
    p2 = p1 # Copiamos referencias
    #apuntan al mismo objeto
    print(p1 is p2) # Imprime True
    
    p1 = Punto3D(4,2,2) 
    p2 = Punto3D(4,2,2)
    #misma informacion
    print(p1 == p2) # Imprime True (NO )
    print(p1 is p2) # Imprime False
    