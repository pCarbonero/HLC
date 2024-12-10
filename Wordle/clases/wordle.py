import random 

class Wordle():
    palabras = ["ANGEL", "JAMON", "LENTO", "VERDE", "PLAYA", "HIELO", "FUEGO", "MANGO", "BANCO", "SALTO"] 
    numIntento = int 

    def __init__(self):
        self.pistas = [["-----","-----"],["-----","-----"],["-----","-----"],["-----","-----"],["-----","-----"],["-----","-----"]]
        self.palabraJuego = ""


    def seleccionaJuego(self):
        index = random.randint(0,9)
        self.palabraJuego = Wordle.palabras[index]

    def realizaIntento(self, intento:str):
        intento = intento.upper()
        
        for fila in range (0,6):
            if self.pistas[fila][0] == "-----":
                self.pistas[fila][0] = intento

                for letra in range(0,5):
                    if self.pistas[fila][1][letra] == '-':
                        if self.palabraJuego[letra] == intento[letra]:
                            prueba = self.pistas[fila][1] 
                            prueba = prueba[:letra] + intento[letra] + prueba[letra+1:]
                            self.pistas[fila][1] = prueba

