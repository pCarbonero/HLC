from Clases.Parchis import *

def test_esGanador1():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 0
    prueba.fichaJ2 = 0
    assert prueba.esGanador() == ""

def test_esGanador2():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 1
    prueba.fichaJ2 = 1
    assert prueba.esGanador() == ""

def test_esGanador3():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 20
    prueba.fichaJ2 = 1
    assert prueba.esGanador() == "Pablo"

def test_esGanador4():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 0
    prueba.fichaJ2 = 20
    assert prueba.esGanador() == "Sara"

def test_esGanador5():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 30
    prueba.fichaJ2 = 1
    assert prueba.esGanador() == ""

def test_esGanador6():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 1
    prueba.fichaJ2 = 30
    assert prueba.esGanador() == ""