from abc import ABCMeta, abstractmethod
from parámetros import *
class Melee(metaclass = ABCMeta):
    def __init__(self, ATP, SHARP, ELEMENT, TYPE_ELEMENT, TYPE, CLASS, VAR, C_I  ):  ####### TYPE * VAR pordria guardarse como uno solo
        self.ATP = float(ATP)
        self.SHARP = SHARP
        self.ELEMENT = float(ELEMENT)
        self.TYPE_ELEMENT = TYPE_ELEMENT
        self.TYPE = TYPE
        self.CLASS = float(CLASS)
        self.VAR = float(VAR)
        self.C_I = C_I

    def dano_base(self):
        pass

    def dano_elemental(self):
        pass

    def dano_cortante(self):
        pass


    def dano_total(self,monster):
        lista_danos = [["---"]]

        for mov in self.Type.keys():
            fila_mov = [mov]

            for zona in monster.zonas:
                if zona not in lista_danos[0] :
                    lista_danos[0].append(zona)

                if self.C_I  == "Both":
                    dano_base = max((self.ATP * self.TYPE[mov]* base_sharp[self.SHARP] * zona[hit_dict["Cut"]] * self.VAR ) / self.CLASS , (self.ATP * self.TYPE[mov]* base_sharp[self.SHARP] * zona[hit_dict["Impact"]] * self.VAR ) / self.CLASS)
                else:
                    dano_base = (self.ATP * self.TYPE[mov] * base_sharp[self.SHARP] * zona[hit_dict[self.C_I]] * self.VAR) / self.CLASS

                dano_elemental = 0

                if self.TYPE_ELEMENT != None:
                    dano_elemental = (self.ELEMENT * elemental_sharp[self.SHARP] * zona[hit_dict[self.TYPE_ELEMENT]] * self.VAR ) / divisor

                fila_mov.append(dano_elemental + dano_base)
            lista_danos.append(fila_mov)

        return lista_danos



class ShieldNSword(Melee):
    def __init__(self,  ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = shield_n_sword_dict["Type"], CLASS = shield_n_sword_dict["Class"], VAR = shield_n_sword_dict["Var"], C_I= "Cut")



class DualSword(Melee):
    def __init__(self,  ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = dual_sword_dict["Type"], CLASS =  dual_sword_dict["Class"], VAR =  dual_sword_dict["Var"], C_I= "Cut")

class GreatSword(Melee):
    def __init__(self,  ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = great_sword_dict["Type"], CLASS = great_sword_dict["Class"], VAR = great_sword_dict["Var"], C_I= "Cut")



