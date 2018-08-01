from SnS import *
from Ayuda import *
from Monstruo import *

#Generar SnS self, base, elem, elem_dano, filo_base, filo_elem

#Generar monstruo cantidad_matriz, matriz
#Generar dano al monstruo  dano_base_arma, tipo_arma, elem, dano_elem_arma

if __name__ == '__main__':
    #Algo asi como main?
    ayuda = Ayuda()
    #Generar lista de monstruos
    ayuda.init_mons()

    #LECTURA DE LAS ARMAS
    
    #COMIENZO DEL LOOP
    while True:
        #PREGUNTAR MONSTRUO
        inp_mons = ayuda.input_monstruos()
        if inp_mons == -1:
            break

        print("\n~~~~~~~~~~~~~~")
        print("Monstruo seleccionado: {0}".format(ayuda.ListaMonstruos[inp_mons].nombre))
        print("~~~~~~~~~~~~~~")

        #PREGUNTAR ARMA
        color = "morado"
        Test = SnS(621, "Hielo", 320, ayuda.filo_base[color], ayuda.filo_elem[color])
        inp_arma = Test.inp()
        if inp_arma == -1:
            break

        #dano_base_arma, tipo_arma, elem, dano_elem_arma
        #Generar daño al monstruo e imprimir
        ayuda.ListaMonstruos[inp_mons].dano_zonas(Test.dano_base_arma(inp_arma),ayuda.arma[Test.arma], Test.elem, Test.dano_elem_arma())


    #FINAL DEL LOOP
    print("\nSaliendo...")
