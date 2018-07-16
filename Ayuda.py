
class Ayuda:
    def __init__(self):
        self.filo_base = {"rojo": 0.5, "naranjo": 0.75, "amarillo": 1, "verde": 1.125, "azul": 1.25, "blanco": 1.3, "morado": 1.5}
        self.filo_elem = {"rojo": 0.25, "naranjo": 0.5, "amarillo": 0.75, "verde": 1, "azul": 1.0625, "blanco": 1.125, "morado": 1.2}

        #Debe existir una mejor forma de hacer esto... 0 cortante, 1 contundente y 2 ambas, aparte en ingles las recuerdo mas
        self.arma = {"SnS": 0, "LS": 0, "GS": 0, "HH": 1, "DS": 0, "HA": 1, "BOW": 1, "LB": 1, "HB": 1, "LA": 2, "GL": 2}
        self.cant_monstruos = 65

    def input_monstruos(self, lista_monstruos):
        print("-1: Salir del programa")
        for i in range(self.cant_monstruos):
            print("{0}: {1}".format(i,lista_monstruos[i].nombre), end = "")

        while True:
            inp = input("Ingrese numero del monstruo a dañar: ")

            try:
                inp = self.lista_mons(inp)
                break
            except Exception as e:
                print("Lo que ha ingresado no coincide con lo pedido")
                print("")
                continue

        return inp

    def lista_mons(self, input):
        #Esto deberia dar un error si no es base 10, asi como el \n
        inp = int(input)
        if inp >= -1 and inp <=64:
            return inp
        else:
            raise AssertionError("Input no coincide")
