import random

class Parchis:
    TAM_TABLERO:int = 20
    dado1 = 0
    dado2 = 0
    
    def __init__(self, nomJ1: str, nomJ2: str):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nomJ1 = nomJ1
        self.nomJ2 = nomJ2

    def tiraDados():
        Parchis.dado1=random.randint(1,6)
        Parchis.dado2=random.randint(1,6)

    def pintaTablero(self):
        tablero = ""

        for l1 in range (0, Parchis.TAM_TABLERO):
            if l1 != 0:
                tablero += "\t"+str(l1)
            else:
                tablero+="\tI"

        tablero += "\tF\n"

        for num in range (1,3):
            if num == 1:
                tablero += self.nomJ1 + "\tI"
                for pos1 in range (1, Parchis.TAM_TABLERO):
                    if self.fichaJ1 == pos1:
                        tablero += "O\t"
                    else:
                        tablero += "\t"
            elif num == 2:
                tablero += self.nomJ2 + "\tI"
                for pos2 in range (1, Parchis.TAM_TABLERO):                 
                    if self.fichaJ2 == pos2:
                        tablero += "O\t"
                    else:
                        tablero += "\t"
            tablero += "\tF\n"
        return tablero
    

    def avanzaPosiciones(self, jugador: int):
        #Parchis.tiraDados()
        if jugador == 1:
            self.fichaJ1 += Parchis.dado1+Parchis.dado2
            if self.fichaJ1 > Parchis.TAM_TABLERO:
                self.fichaJ1 = Parchis.TAM_TABLERO - (self.fichaJ1-Parchis.TAM_TABLERO)
        elif jugador == 2:
            self.fichaJ2 += Parchis.dado1+Parchis.dado2
            if self.fichaJ2 > Parchis.TAM_TABLERO:
                self.fichaJ2 = Parchis.TAM_TABLERO - (self.fichaJ2-Parchis.TAM_TABLERO)


    def estadoCarrera(self):
        ganador = "Va ganando "

        if self.fichaJ1 > self.fichaJ2:
           ganador += self.nomJ1
        elif self.fichaJ2 > self.fichaJ1:
           ganador += self.nomJ2
        else: ganador = "Vais empatados"

        return ganador
    
    def esGanador(self):
        ganador = ""

        if self.fichaJ1 == Parchis.TAM_TABLERO:
           ganador = self.nomJ1
        elif self.fichaJ2 == Parchis.TAM_TABLERO:
           ganador = self.nomJ2

        return ganador