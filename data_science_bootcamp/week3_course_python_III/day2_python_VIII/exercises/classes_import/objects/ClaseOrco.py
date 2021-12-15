class Orco():

    def __init__(self,  nombre, armadura, nivel, ataque, ojos=2, piernas=2, dientes=56, salud=100):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud

    
    def atacar(self,humano):
        humano.salud -= self.ataque - humano.armadura
        print("La salud del Humano es", humano.salud)

    
    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def mostrar_atributos(self):
        print("nombre:", self.nombre, "/", "dientes:", self.dientes, "/", "ojos:", self.ojos, 
        "/", "piernas:", self.piernas, "/", "armadura:", self.armadura, "/", "nivel:", self.nivel, "/", "ataque:",
        self.ataque, "/", "salud",self.salud)

