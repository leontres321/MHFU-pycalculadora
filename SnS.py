from Melee import *

#TODO ver el cambio de var para las lanzas
#AssertionError porque solo recordaba ese
class SnS(Arma_melee):
    def __init__(self, base, elem, elem_dano, filo_base, filo_elem):
        super().__init__(base, elem, elem_dano, filo_base, filo_elem, clase = 1.4, var = 1)
        self.movimiento = [.46, .27, .18, .15, .15, .14, .18]
        self.arma = "SnS"

    def input_correcto(self):
        var = int(input("Ingrese un numero de los antes listados: "))
        if var >= -1 and var <=7:
            return var
        else:
            raise AssertionError("Input incorrecto")

    def inp(self):
        print("-1: Salir del programa")
        print("0: Combo regular")
        print("1: Corte giratorio")
        print("2: Corte con saltando")
        print("3: Corte luego de rodar")
        print("4: Ataque con bloqueo 1")
        print("5: Ataque con bloqueo 2")
        print("6: Corte desenfundando")
        print("7: Escoger denuevo")

        #intento de algo decente... ok esta re malo pero almenos hace el trabajo
        while True:
            try:
                input = self.input_correcto()
                break
            except AssertionError as e:
                print("Por favor vuelve a ingresar el numero\n")
                continue
        return input
