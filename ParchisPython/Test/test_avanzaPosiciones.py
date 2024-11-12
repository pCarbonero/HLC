from Clases.Parchis import *

def test_avanzaposiciones1():
    prueba = Parchis("Pablo", "Sara")
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    prueba.avanzaPosiciones(1)
    assert prueba.fichaJ1 == 2

def test_avanzaposiciones2():
    prueba = Parchis("Pablo", "Sara")
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    prueba.avanzaPosiciones(2)
    assert prueba.fichaJ2 == 2

def test_avanzaposiciones3():
    prueba = Parchis("Pablo", "Sara")
    Parchis.dado1 = 6
    Parchis.dado2 = 6
    prueba.avanzaPosiciones(1)
    assert prueba.fichaJ1 == 12

def test_avanzaposiciones4():
    prueba = Parchis("Pablo", "Sara")
    Parchis.dado1 = 6
    Parchis.dado2 = 6
    prueba.avanzaPosiciones(2)
    assert prueba.fichaJ2 == 12

def test_avanzaposiciones5():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 5
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    prueba.avanzaPosiciones(1)
    assert prueba.fichaJ1 == 7


def test_avanzaposiciones6():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ2 = 7
    Parchis.dado1 = 1
    Parchis.dado2 = 1
    prueba.avanzaPosiciones(2)
    assert prueba.fichaJ2 == 9

def test_avanzaposiciones7():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 15
    Parchis.dado1 = 3
    Parchis.dado2 = 3
    prueba.avanzaPosiciones(1)
    assert prueba.fichaJ1 == 19


def test_avanzaposiciones8():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ2 = 18
    Parchis.dado1 = 2
    Parchis.dado2 = 4
    prueba.avanzaPosiciones(2)
    assert prueba.fichaJ2 == 16