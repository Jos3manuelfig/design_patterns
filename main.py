
class Casa:
    def __init__(self,):
        self.puertas = 0
        self.ventanas = 0
        self.techo = False


    def __str__(self):
        techo_str =  " Con techo" if self.techo else "sin techo"
        return f" Casa con: {self.puertas} puertas, {self.ventanas} ventnas, {techo_str}"



class CasaBuilder:
    def __init__(self):
        self.casa = Casa()


    def agregar_puertas(self, numero):
        self.casa.puertas = numero
        return self

    def agregar_ventanas(self, numero):
        self.casa.ventanas = numero
        return  self

    def contruir_techo(self):
        self.casa.techo = True
        return self

    def obtener_casa(self):
        return  self.casa



class DirectorCasa:
    def __init__(self, builder):
        self.builder = builder

    def constrir_Casa_Completa(self):
        return (self.builder
                .agregar_puertas(5)
                .agregar_ventanas(6)
                .contruir_techo()
                .obtener_casa()

                )

builder = CasaBuilder()
director = DirectorCasa(builder)
casa = director.constrir_Casa_Completa()
print(casa)
