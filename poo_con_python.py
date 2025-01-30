class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.inventario = {"1": 0, "2": 0, "3": 0}
        self.tipo_pocima_seleccionada = None

    def imprimir_atributos(self):
        print(self.nombre)
        print("- Fuerza:", self.fuerza)
        print("- Inteligencia:", self.inteligencia)
        print("- Defensa:", self.defensa)
        print("- Vida:", self.vida)

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto.")

    def recibir_ataque(self, daño):
        self.vida -= daño
        print(self.nombre, "recibió", daño, "de daño. Vida restante:", self.vida)
        if not self.esta_vivo():
            self.morir()

    def atacar(self, enemigo):
        daño = max(self.fuerza - enemigo.defensa, 0)
        enemigo.recibir_ataque(daño)

    def añadir_pocima(self):
        tipo = input("Escoge tu poción: \n(1) Vida\n(2) Fuerza\n(3) Inteligencia\n")
        if tipo in self.inventario:
            self.inventario[tipo] += 1
            print("Has añadido una pócima de tipo", tipo)
        else:
            print("Opción no válida.")

    def usar_pocima(self):
        tipo = input("¿Qué tipo de pócima quieres usar? (1, 2, 3): ")
        if tipo in self.inventario and self.inventario[tipo] > 0:
            self.inventario[tipo] -= 1
            if tipo == "1":
                self.vida += 20
                print(f"{self.nombre} usó una pócima de vida. Vida ahora: {self.vida}.")
            elif tipo == "2":
                self.fuerza = int(self.fuerza * 1.5)
                print(f"{self.nombre} usó una pócima de fuerza. Fuerza ahora: {self.fuerza}.")
            elif tipo == "3":
                self.inteligencia = int(self.inteligencia * 1.5)
                print(f"{self.nombre} usó una pócima de inteligencia. Inteligencia ahora: {self.inteligencia}.")
        else:
            print("No tienes esa pócima.")

    @staticmethod
    def suma_inteligencia(personajes):
        return sum(personaje.inteligencia for personaje in personajes)


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada=0, escudo=0):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        self.escudo = escudo

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("- Espada:", self.espada)
        print("- Escudo:", self.escudo)

    def elegir_arma(self):
        opcion = int(input("Elige un arma:\n(1) Lanza de obsidiana (daño 10)\n(2) Lanza de chaya (daño 5)\n"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 5
        else:
            print("Opción no válida.")
            self.elegir_arma()

    def recibir_ataque(self, daño):
        if self.escudo > daño:
            self.escudo -= daño
            print(f"El escudo de {self.nombre} absorbió el daño. Escudo restante: {self.escudo}.")
        else:
            daño_restante = daño - self.escudo
            self.escudo = 0
            super().recibir_ataque(daño_restante)


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro=0):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("- Libro:", self.libro)

    def elegir_arma(self):
        opcion = int(input("Elige un arma:\n(1) Hechizos de programación (daño 10)\n(2) Recetario de chaya (daño 2)\n"))
        if opcion == 1:
            self.libro = 10
        elif opcion == 2:
            self.libro = 2
        else:
            print("Opción no válida.")
            self.elegir_arma()


# Crear personajes
michael_jackson = Personaje("Michael Jackson", 2000, 15, 10, 100)
tlatoani = Guerrero("Tlatoani", 50, 70, 30, 100)
merlin = Mago("Merlín", 20, 15, 10, 100)

# Sumar inteligencia de los personajes
personajes = [michael_jackson, tlatoani, merlin]
inteligencia_total = Personaje.suma_inteligencia(personajes)
print("La inteligencia total de los personajes es:", inteligencia_total)

# Filtrar personajes por vida
valor_vida = int(input("Introduce un valor de vida para filtrar personajes: "))
personajes_filtrados = [p for p in personajes if p.vida > valor_vida]

if personajes_filtrados:
    print("Personajes con vida mayor a", valor_vida, ":")
    for p in personajes_filtrados:
        print("-", p.nombre, "con", p.vida, "de vida.")
else:
    print("No hay personajes con vida mayor a", valor_vida, ".")

# Prepararse para la guerra
print("\nPREPARACIÓN PARA LA GUERRA")
for personaje in personajes:
    personaje.añadir_pocima()
    personaje.usar_pocima()
    personaje.imprimir_atributos()
