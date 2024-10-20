# main.py

from typing import Iterable, Optional
from comandos import *
from personajes import *

class Juego:
    def __init__(self) -> None:
        self._pelea: Optional[Iterable[Comando]] = None

    def set_pelea(self, comandos: Iterable[Comando]) -> None:
        self._pelea = comandos

    def ejecutar(self) -> None:
        if self._pelea is not None:
            for comando in self._pelea:
                comando.ejecutar()

if __name__ == "__main__":
    juego = Juego()
    paladin = Paladin()
    elfo1 = Elfo()
    elfo2 = Elfo()
    enemigo1 = Nigromantes()
    enemigo2 = Orcos()
    enemigo3 = Orcos()
    mago = Elfo()  # Asumiendo que Elfo implementa Mago

    pelea = [
        AtacarEnemigo(enemigo1),
        Defenderse(paladin),
        SanarAliado(elfo1),
        UsarObjeto(mago, "Poción de Vida"),
        InvocarAliado(mago, "Espíritu Guardián"),
        AtacarEnemigo(enemigo2),
        AtacarEnemigo(paladin),
        AtacarEnemigo(enemigo3),
        AtacarEnemigo(elfo2)
    ]

    juego.set_pelea(pelea)
    juego.ejecutar()
