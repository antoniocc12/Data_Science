import os  
import sys

ruta = __file__

print(ruta)

for i in range(4):
    ruta = os.path.dirname(ruta)
    print(ruta)

sys.path.append(ruta)


import imports.a.x as fun2
import imports.b.y as fun3

a = [4, 7]
b = [21, 89]



def f1z():
    print("El nombre de la función es", "f1z")
    fun3.f1y()



def f2z():
    print("El nombre de la función es", "f2z")
    fun2.f2x()

f1z()
f2z()