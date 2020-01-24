from abc import ABCMeta, abstractmethod
from parámetros import *
class Melee(metaclass = ABCMeta):
    def __init__(self, ATP, SHARP, ELEMENT, TYPE_ELEMENT, TYPE, CLASS, VAR, C_I  ):  ####### TYPE * VAR pordria guardarse como uno solo

        self.TYPE_ELEMENT = TYPE_ELEMENT
        self.TYPE = TYPE
        self.VAR = VAR
        self.C_I = C_I
        self.AUX_BASE = float(ATP) * base_sharp[SHARP] / float(CLASS)
        self.AUX_ELEM = float(ELEMENT) * elemental_sharp[SHARP] / divisor

    def dano_total(self,monster):
        lista_danos = [["---"]]

        for mov in self.Type.keys():
            fila_mov = [mov]

            for zona in monster.zonas:
                if zona not in lista_danos[0] :
                    lista_danos[0].append(zona)

                if self.C_I  == "Both":
                    dano_base = max(self.AUX_BASE * self.TYPE[mov] *  zona[hit_dict["Cut"]] * self.VAR ,
                                    self.AUX_BASE * self.TYPE[mov] * zona[hit_dict["Impact"]] * self.VAR )
                else:
                    dano_base = self.AUX_BASE * self.TYPE[mov] *  zona[hit_dict[self.C_I]] * self.VAR

                dano_elemental = 0

                if self.TYPE_ELEMENT != None:
                    dano_elemental = self.AUX_ELEM *  zona[hit_dict[self.TYPE_ELEMENT]] * self.VAR

                fila_mov.append(dano_elemental + dano_base)
            lista_danos.append(fila_mov)

        return lista_danos

    def dano_raro(self,monster):
        lista_danos = [["---"]]

        for mov in self.Type.keys():
            fila_mov = [mov]

            if "All" in self.VAR.keys():
                var_1 = self.VAR["All"]
            elif mov in self.VAR.keys():
                var_1 = self.VAR[mov]
                var_2 = self.VAR[mov]
            elif mov in ["Charging Stab Finisher", "Charge Through"]:
                var_1 = self.VAR["Charging Cut"]
                var_2 = self.VAR["Charging Impact"]
            else:
                var_1 = 1
                var_2= 1

            for zona in monster.zonas:
                if zona not in lista_danos[0]:
                    lista_danos[0].append(zona)

                if self.C_I == "Both":
                    dano_base = max(self.AUX_BASE * self.TYPE[mov] * zona[hit_dict["Cut"]] * var_1,
                                    self.AUX_BASE * self.TYPE[mov] * zona[hit_dict["Impact"]] * var_2)
                else:
                    dano_base = self.AUX_BASE * self.TYPE[mov] * zona[hit_dict[self.C_I]] * var_1

                dano_elemental = 0

                if self.TYPE_ELEMENT != None:
                    dano_elemental = self.AUX_ELEM * zona[hit_dict[self.TYPE_ELEMENT]] * var_1 ## que var usa lanza segun si antes es cut o imp

                fila_mov.append(dano_elemental + dano_base)
            lista_danos.append(fila_mov)

        return lista_danos



class ShieldNSword(Melee):
    def __init__(self,  ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = shield_n_sword_dict["Type"], CLASS = shield_n_sword_dict["Class"], VAR = shield_n_sword_dict["Var"], C_I= "Cut")



class DualSword(Melee):
    def __init__(self,  ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = dual_sword_dict["Type"], CLASS =  dual_sword_dict["Class"], VAR =  dual_sword_dict["Var"], C_I= "Cut")
"""
class GreatSword(Melee):
    def __init__(self,  ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = great_sword_dict["Type"], CLASS = great_sword_dict["Class"], VAR = great_sword_dict["Var"], C_I= "Cut")
"""
class GunLance(Melee):
    def __init__(self,  ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = gunlance_dict["Type"], CLASS = gunlance_dict["Class"], VAR = gunlance_dict["Var"], C_I= "Cut")

class Hammer(Melee):
    def __init__(self, ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP = ATP, SHARP = SHARP, ELEMENT = ELEMENT, TYPE_ELEMENT = TYPE_ELEMENT, TYPE = hammer_dict["Type"], CLASS = hammer_dict["Class"], VAR = hammer_dict["Var"], C_I= "Impact")

class HuntingHorn(Melee):
    def __init__(self, ATP, SHARP, ELEMENT, TYPE_ELEMENT):
        super().__init__(ATP=ATP, SHARP=SHARP, ELEMENT=ELEMENT, TYPE_ELEMENT=TYPE_ELEMENT, TYPE=hunting_horn_dict["Type"],
                         CLASS=hunting_horn_dict["Class"], VAR=hunting_horn_dict["Var"], C_I="Impact")

