class Personaje:
    # El método constructor debe llamarse __init__
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print("- Nombre: ", self.nombre)
        print("- Fuerza: ", self.fuerza)
        print("- Inteligencia: ", self.inteligencia)
        print("- Defensa: ", self.defensa)
        print("- Vida: ", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0 
        print(self.nombre, "ha muerto")

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado un ataque RAAAAAA. Ya muerete ", enemigo.nombre)
        print(self.nombre, "ha realizado ", daño, " puntos de daño a ", enemigo.nombre)
        print("Vida restante de ", enemigo.nombre, " es de ", enemigo.vida)

class Guerrero(Personaje):
    pass

tlotoani = Guerrero ("Apocalimpto",50, 70, 30, 100)

# Crear un personaje
mi_personaje = Personaje("EdierUwU", 100, 3, 70, 100)
mi_personaje.imprimir_atributos()

# Crear un enemigo
mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)

# Realizar un ataque
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()
