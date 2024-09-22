from abc import  ABC, abstractmethod
from typing import Optional, Union

class Combatiente(ABC):
    @abstractmethod
    def pelear(self):
        pass
class Mago(ABC):
    @abstractmethod
    def sanar(self):
        pass
    @abstractmethod
    def invocar_Hechizo(self):
        pass


class Paladin(Combatiente):
    def pelear(self):
        print("Paladin pelenado con espada")


class Orcos(Combatiente):
    def pelear(self):
        print("Paladin pelenado con piedras")

class Elfo(Mago):

    def sanar(self):
        print("Elfo SAnando Aliados")

    def invocar_Hechizo(self):
        print("Elfo lanzanod hechizo")


class Nigromantes(Mago):
    def sanar(self):
        pass

    def invocar_Hechizo(self):
        print("Nigromantes lanzando hechizo")