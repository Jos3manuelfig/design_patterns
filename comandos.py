# comandos.py

from abc import ABC, abstractmethod
from typing import Union
from personajes import *

class Comando(ABC):
    @abstractmethod
    def ejecutar(self) -> None:
        pass

class AtacarEnemigo(Comando):
    def __init__(self, personaje: Union[Combatiente, Mago]) -> None:
        self._personaje = personaje

    def ejecutar(self) -> None:
        if isinstance(self._personaje, Combatiente):
            self._personaje.pelear()
        elif isinstance(self._personaje, Mago):
            self._personaje.invocar_Hechizo()

class SanarAliado(Comando):
    def __init__(self, mago: Mago) -> None:
        self._personaje = mago

    def ejecutar(self) -> None:
        self._personaje.sanar()

# Nuevo comando: Defenderse
class Defenderse(Comando):
    def __init__(self, personaje: Combatiente) -> None:
        self._personaje = personaje

    def ejecutar(self) -> None:
        print(f"{self._personaje.__class__.__name__} se está defendiendo.")

# Nuevo comando: Usar Objeto
class UsarObjeto(Comando):
    def __init__(self, personaje: Mago, objeto: str) -> None:
        self._personaje = personaje
        self._objeto = objeto

    def ejecutar(self) -> None:
        print(f"{self._personaje.__class__.__name__} usa el objeto: {self._objeto}.")

# Nuevo comando: Invocar Aliado
class InvocarAliado(Comando):
    def __init__(self, mago: Mago, aliado: str) -> None:
        self._mago = mago
        self._aliado = aliado

    def ejecutar(self) -> None:
        print(f"{self._mago.__class__.__name__} invoca a {self._aliado}.")
