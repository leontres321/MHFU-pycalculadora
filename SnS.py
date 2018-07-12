from Melee import *

#TODO ver si se puede dejar de una manera más bonita, TODO ver el cambio de var para las lanzas
class SnS(Arma_melee):
    def __init__(self, base, elem, elem_dano, filo_base, filo_elem):
        super().__init__(base, elem, elem_dano, filo_base, filo_elem, clase = 1.4, var = 1)
        self.movimiento = [.46, .27, .18, .15, .15, .14, .18]
        self.arma = "SnS"

    def dano_base(self):
        print("0: Combo regular")
        print("1: Corte giratorio")
        print("2: Corte saltandor")
        print("3: Corte luego de rodar")
        print("4: Ataque con bloqueo 1")
        print("5: Ataque con bloqueo 2")
        print("6: Corte desenfundando")

        #intento de algo decente
        while True:
            try:
                input = self.input_correcto()
                break
            except Exception as e:
                print("Por favor vuelve a ingresar el numero")
                continue

        return self.base * self.movimiento[input] * self.filo_base * self.var / self.clase

    def input_correcto(self):
        var = int(input("Ingrese un numero de los antes listados: "))
        if var >= 0 and var <=6:
            return var
        else:
            raise AssertionError("Input incorrecto")
