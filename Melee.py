from abc import ABCMeta, abstractmethod

class Arma_melee(metaclass = ABCMeta):
    def __init__(self, base, elem, elem_dano, filo_base, filo_elem, clase, var):
        self.base = base
        self.elem_dano = elem_dano
        self.elem = elem
        self.filo_base = filo_base
        self.filo_elem = filo_elem
        self.clase = clase
        self.var = var

    #Esto es abstracto por la variable type, que refiere al movimiento del ataque
    @abstractmethod
    def dano_base(self, input):
        pass

    def dano_elem(self):
        return self.elem * self.filo_elem * self.var / 10

    @abstractmethod
    def input_correcto(self):
        pass
