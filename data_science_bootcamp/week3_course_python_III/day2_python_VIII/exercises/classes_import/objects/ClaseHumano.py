class Humano ():

    def __init__(self,  nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=32, salud=100):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

#Esta función resta a la vida del 'Orco' el ataque de 'Humano' 
# menos la armadura de 'Orco'. Al final, muestra por pantalla la vida del 
# 'Orco'
    def atacar(self,orco):
        
        orco.salud -= self.ataque - orco.armadura
        print("La salud del Orco es", orco.salud)

#Una función no_vivo que retorna True si la vida del 'Humano' 
# es igual o inferior a 0, False en otro caso. 

    def no_vivo(self):
        self.salud
        if self.salud <= 0:
            return True
        else:
            return False

    
#Una función que muestre por pantalla todos los atributos 
# actuales de 'Humano' concatenados con un String representando 
# el nombre del atributo que se muestra. Ejemplo: "Nombre: 
# Ataulfo | dientes: 32 | salud: 100 | ..."

    def mostrar_atributos(self):
        print("nombre:", self.nombre, "/", "dientes:", self.dientes, "/", "ojos:", self.ojos, 
        "/", "piernas:", self.piernas, "/", "armadura:", self.armadura, "/", "nivel:", self.nivel, "/", "ataque:", self.ataque, "/", "salud",self.salud)
  
       




