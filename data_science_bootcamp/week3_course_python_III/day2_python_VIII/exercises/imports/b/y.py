import os  
import sys

ruta = __file__

print(ruta)

for i in range(3):
    ruta = os.path.dirname(ruta)
    print(ruta)

sys.path.append(ruta)


import imports.a.x as fun1


a = [24, 5]
b = (5, "casa")

#La función "f1y" que has creado en el archivo 'y.py' debe 
# llamar a la función "f1x" del archivo 'x.py'
def f1y():
    print("El nombre de la función es", "f1y")
    fun1.f1x()



#La función "f2y" debe llamar a la función 'f2x'

def f2y():
    print("El nombre de la función es", "f2y")
    fun1.f2x()

f1y()
f2y()


