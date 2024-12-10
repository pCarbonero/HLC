from clases.wordle import *

def test_seleccionaJuego1():
    wordle = Wordle()
    wordle.seleccionaJuego()
    assert wordle.palabraJuego in wordle.palabras
