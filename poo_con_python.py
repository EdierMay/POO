class Personaje:
    # El método constructor debe llamarse __init__
    def __init__(self, __nombre, __fuerza, __inteligencia, __defensa, __vida):
        self.__nombre = __nombre
        self.__fuerza = __fuerza
        self.__inteligencia = __inteligencia
        self.__defensa = __defensa
        self.__vida = __vida

    def imprimir_atributos(self):
        print("- __nombre: ", self.__nombre)
        print("- __fuerza: ", self.__fuerza)
        print("- __inteligencia: ", self.__inteligencia)
        print("- __defensa: ", self.__defensa)
        print("- __vida: ", self.__vida)
    
    def subir_nivel(self, __fuerza, __inteligencia, __defensa):
        self.__fuerza += __fuerza
        self.__inteligencia += __inteligencia
        self.__defensa += __defensa

    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0 
        print(self.__nombre, "ha muerto")

    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida -= daño
        print(self.__nombre, "ha realizado un ataque RAAAAAA. Ya muerete ", enemigo.__nombre)
        print(self.__nombre, "ha realizado ", daño, " puntos de daño a ", enemigo.__nombre)
        print("__vida restante de ", enemigo.__nombre, " es de ", enemigo.__vida)

    def get_fuerza(self):
            return self.__fuerza

    def set_fuerza(self,fuerza):
            if fuerza <0:
                print("Error, valor negativo")
            else: self.__fuerza = fuerza

# Crear un personaje
mi_personaje = Personaje("EdierUwU", 100, 3, 70, 100)
#mi_personaje.imprimir_atributos()

# Crear un enemigo
mi_enemigo = Personaje("Vergil", 70, 30, 70, 100)

# Realizar un ataque
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()

#mi_personaje.__fuerza
#mi_personaje.fuerza = 0
#mi_personaje.imprimir_atributos

mi_personaje.set_fuerza(-5)
print(mi_personaje.get_fuerza())
