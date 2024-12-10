from clases.wordle import *

def test_realizaIntento1():
    wordle = Wordle()
    wordle.palabraJuego = "PLAYA"
    wordle.realizaIntento("Pablo")
    
    assert wordle.pistas[0][0] == "PABLO" and wordle.pistas[0][1] == "P----"


