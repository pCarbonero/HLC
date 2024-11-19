from Clases.Parchis import *

def test_estadoCarrera0():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 0
    prueba.fichaJ2 = 0
    assert prueba.estadoCarrera() == "Vais empatados"


def test_estadoCarrera1():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 2
    prueba.fichaJ2 = 0
    assert prueba.estadoCarrera() == "Va ganando Pablo"

def test_estadoCarrera2():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 2
    prueba.fichaJ2 = 8
    assert prueba.estadoCarrera() == "Va ganando Sara"


def test_estadoCarrera3():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 0
    prueba.fichaJ2 = 0
    assert prueba.estadoCarrera() == "Vais empatados"

def test_estadoCarrera4():
    prueba = Parchis("Pablo", "Sara")
    prueba.fichaJ1 = 20
    prueba.fichaJ2 = 0
    assert prueba.estadoCarrera() == "Va ganando Pablo"