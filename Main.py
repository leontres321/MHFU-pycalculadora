from SnS import *
from Ayuda import *
from Monstruo import *

#Generar SnS self, base, elem, elem_dano, filo_base, filo_elem

#Generar monstruo cantidad_matriz, matriz
#Generar dano al monstruo  dano_base_arma, tipo_arma, elem, dano_elem_arma

if __name__ == '__main__':
    #Tablas de ayuda, se usan para las armas
    tablas = Ayuda()
    #lista de todos los monstruos
    ListaMonstruos = []

    #LECTURA DEL ARCHIVO DE MONSTRUOS TODO VER SI HACER UNA FUNCION PARA LIMPIAR MAIN
    arch = open("ListaMonstruos.txt","r")
    for i in range(65):
        #lectura de una linea
        linea = arch.readline()
        #Separacion de primera linea
        mon_cant = int(linea[0])
        mon_nombre = linea[2:]
        mon_matriz = []
        #leer lineas que tenga el bichito bonito
        for j in range(mon_cant):
            linea = arch.readline()
            lista = linea.split()
            nuevo = []

            for m in lista:
                try:
                    nuevo.append(float(m))
                except ValueError:
                    nuevo.append(m)

            mon_matriz.append(nuevo)

        #Lectura de linea vacia
        arch.readline()
        #Generar un objeto monstruo
        ListaMonstruos.append(Monstruo(mon_nombre, mon_cant, mon_matriz, 0.75, 1))
    arch.close()
    #LECTURA DE LAS ARMAS

    #COMIENZO DEL LOOP
    while True:
        #PREGUNTAR MONSTRUO
        inp_mons = tablas.input_monstruos(ListaMonstruos)
        if inp_mons == -1:
            break

        print("\n~~~~~~~~~~~~~~")
        print("Monstruo seleccionado: {0}".format(ListaMonstruos[inp_mons].nombre))
        print("~~~~~~~~~~~~~~")

        #PREGUNTAR ARMA
        Test = SnS(196, "Dragon", 520, tablas.filo_base["blanco"], tablas.filo_elem["blanco"])
        inp_arma = Test.inp()
        if inp_arma == -1:
            break

        #dano_base_arma, tipo_arma, elem, dano_elem_arma
        #Generar daño al monstruo e imprimir
        ListaMonstruos[inp_mons].dano_zonas(Test.dano_base_arma(inp_arma),tablas.arma[Test.arma], Test.elem, Test.dano_elem_arma())


    #FINAL DEL LOOP
    print("\nSaliendo...")
