# Producto: La clase Casa que queremos construir
class Casa:
    def __init__(self):
        self.puertas = 0
        self.ventanas = 0
        self.techo = False

    def __str__(self):
        techo_str = "con techo" if self.techo else "sin techo"
        return f"Casa con {self.puertas} puertas, {self.ventanas} ventanas, {techo_str}."


# Builder: Define la interfaz para construir una Casa
class CasaBuilder:
    def __init__(self):
        self.casa = Casa()

    def agregar_puertas(self, numero):
        self.casa.puertas = numero
        return self

    def agregar_ventanas(self, numero):
        self.casa.ventanas = numero
        return self

    def construir_techo(self):
        self.casa.techo = True
        return self

    def obtener_casa(self):
        return self.casa


# Director: Controla el proceso de construcción de la Casa
class DirectorCasa:
    def __init__(self, builder):
        self.builder = builder

    def construir_casa_completa(self):
        return (self.builder
                .agregar_puertas(4)
                .agregar_ventanas(6)
                .construir_techo()
                .obtener_casa())


# Uso del patrón Builder
if __name__ == "__main__":
    builder = CasaBuilder()
    director = DirectorCasa(builder)

    # El director construye la casa paso a paso
    casa = director.construir_casa_completa()
    print(casa)  # Output: Casa con 4 puertas, 6 ventanas, con techo.
