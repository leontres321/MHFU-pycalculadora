#Hacer esto para cada arma y contener los combos
class Arma_melee:
    #ver si poner o no var aca, por la falta de var
    def __init__(self, base, elem, filo, critico, clase):
        self.base = base
        self.elem = elem
        self.filo = filo
        self.critico = critico
        self.clase = clase

    def dano_base(self, tipo, filo_base, zona, defensa, ira, var):
        return int(self.base * tipo * filo_base * zona * defensa * ira * var / self.clase)

    def dano_elem(self, filo_elem, Ezona, defensa, ira, var):
        return int(self.elem * filo_elem * Ezona * defensa * ira * var / 10)
