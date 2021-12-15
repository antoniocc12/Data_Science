#import os  
#import sys

#ruta = __file__

#for i in range(3):
    #ruta = os.path.dirname(ruta)
    #print(ruta)

#sys.path.append(ruta)

#import imports.b.c.z as fun4

a = [1, "hola"]
b = [35, (34, "mundo")]

def f1x():
    print("El nombre de la función es", "f1x")


#La función "f2x" debe llamar a la función 'f2z'

def f2x():
    print("El nombre de la función es", "f2x")
    #fun4.f2z() Esta función da error por que genera un blucle infinito

f1x()
f2x()




