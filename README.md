# MHFU-pycalculadora
Intento de calculadora en python para el juego MHFU


# Metas
- ~~Calcular el daño de espada y escudo ante un monstruo~~
- ~~Cambiar el monstruo con el que se pelea~~
- Escoger espadas y escudos dentro del programa
- Cambiar el tipo de arma
- Bonus de comida, habilidades y objetos
- Hacer el codigo como un ser humano pensante... o almenos intentarlo
- Intefaz gráfica (jajaja)


# ¿Alguien sigue jugando MHFU en 2018?
Pues tal vez no mucha gente ,pero, almenos con mis amigos jugamos y al ver que nos falta una calculadora para poder asesinar
 y vestirnos con escamas lujosas de una forma eficiente... pues ahí nace la idea... esperemos que la termine.

# ¿De dónde sale la información?
De estas tres paginas de **GameFAQs**:\
[Para c/c](https://gamefaqs.gamespot.com/psp/943356-monster-hunter-freedom-unite/faqs/53339)\
[Para Arco](https://gamefaqs.gamespot.com/psp/943356-monster-hunter-freedom-unite/faqs/57883)\
[Para ballesta](https://gamefaqs.gamespot.com/psp/943356-monster-hunter-freedom-unite/faqs/57865)

# Versiones:
  - v0.2.1
    - Se arreglo el daño para el hielo, se hizo una funcion para inicializacion de los monstruos para limpiar main
  - v0.2.0
    - Se arregló la inicializacion de monstruos ya que la lista de zonas estaba mal generada, se puede generar del daño de una Espada y Escudo (está en el código) a todos los monstros grandes del juego.
  - v0.1.2
    - Se eliminó la carpeta de monstruos y se generó un archivo con todos estos, ademas fueron ingresados al código y se comenzó la funcion de calculo de daño e impresión
  - v0.1.1
    - Se creó una carpeta para monstruos y se comenzó a trabajar con metodos, ademas se hizo una subclase para las espadas y escudos.
  - v0.1.0
    - Se agregaron clases para poder la hacer la calculadora de una forma "bonita" (clases de python) y se dividió el código
  - v0.0.1
    - Version inicial de la calculadora, tan solo se probó la formula para c/c

# Problemas actuales:
- Imprimir decentemente
- Dejar espacio para que sea legible la impresion de daños y no que deba ser buscada
- Saber generar el número de la versión...

# Notas:
- Se eliminó tablas duplicadas del Daimyo Hermitaur (tambien sub especies), esto se debe a que para una zona existian dos valores (pinzas rotas o no)... quitar esta tabla me simplifica la vida
- Buscando informacion de la defensa de los monstruos me encontré de que en el MHF1 la defensa es variable, pero tambien me encontré que la defensa en offline siempre es 1 y que en online varía, tambien leí que varía según la mision específica, por lo tanto **todos los monstruos serán de rango G** y se supondrá que la defensa es 0.75
- Por el momento los monstruos no tendrán estado de ira (haciendo que esta variable sea 1 simpre)
- Para el cálculo de daño se toma el piso de los valores calculados, esto se debé a que en algun lugar vi que se hacia así...

# Como se suman los bonificadores:
Hace unos años busqué como se apilan los bonificadores de ataque (comida, objetos y más) por lo que lo dejaré aquí para no olvidarlo. Las Categorías se suman pero solo puede haber un bonificador activo en cada Categoría por lo que si tomas una Droga Demoniaca y una MegaDroga Demoniaca estas no se suman y solo se toma la mayor. \
[Categoría 1] Amuletos \
[Categoría 2] Garras \
[Categoría 3] Semilla de Poder, Píldora de Poder o Flauta Demonio \
[Categoría 4] Droga Demoniaca, MegaDroga Demoniaca o Cocina Felyne \
[Categoría 5] Aumento Ataque [Bajo]/[Medio]/[Alto] por la Armadura \
[Categoría 6] Cuerno de Caza: Aumento Ataque [Bajo x1], [Bajo x2] o [Alto x1], [Alto x2]



# Ayuda visual de la formula de daño
![Arbol dano](calculadora.png)