from Melee import *
import Monstruo

#TODO guardar el filo en el arma y solo revisar el diccionario al crear esta
if __name__ == '__main__':
    #(self, base, elem, filo, critico, clase)
    SnS = Arma_melee(196, 520, "blanco", 0, 1.4)
    filo_base = {"rojo": 0.5, "naranjo": 0.75, "amarillo": 1, "verde": 1.125, "azul": 1.25, "blanco": 1.3, "morado": 1.5}
    filo_elem = {"rojo": 0.25, "naranjo": 0.5, "amarillo": 0.75, "verde": 1, "azul": 1.0625, "blanco": 1.125, "morado": 1.2}

    #(self, tipo, filo_base, zona, defensa, ira, var)
    dano_base = SnS.dano_base(0.18, filo_base[SnS.filo], 0.8, 1, 1, 1)

    #(self, filo_elem, Ezona, defensa, ira, var)
    dano_elem = SnS.dano_elem(filo_elem[SnS.filo], 0.3, 1, 1, 1)


    print("Prueba de Sns saltando vs Rathalos G:")
    print("Daño base: ", dano_base, ", Daño elemental: ", dano_elem)
    print("Total: ", dano_base + dano_elem)
