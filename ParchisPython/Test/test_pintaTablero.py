from Clases.Parchis import *                                        

def test_pintaTablero1():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Pablo\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "Sara\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"     
    prueba = Parchis("Pablo", "Sara")
    tableroPrueba = prueba.pintaTablero()
    assert prueba.pintaTablero() == tablero

def test_pintaTablero2():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Pablo\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"     
    prueba = Parchis("Pablo", "")
    tableroPrueba = prueba.pintaTablero()
    assert prueba.pintaTablero() == tablero

def test_pintaTablero3():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "rtgjghighadfg\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "rrrrrrrrrrrrrrrrrrrrrrrrrr   $%&$\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"     
    prueba = Parchis("rtgjghighadfg", "rrrrrrrrrrrrrrrrrrrrrrrrrr   $%&$")
    tableroPrueba = prueba.pintaTablero()
    assert prueba.pintaTablero() == tablero
