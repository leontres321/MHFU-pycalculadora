# MHFU-pycalculadora
Intento de calculadora en python para el juego MHFU


# Metas
- ~~Calcular el daño de espada y escudo ante un monstruo~~
- Hacer el codigo como un ser humano pensante... o almenos intentarlo
- Escoger espadas y escudos dentro del programa
- Cambiar el monstruo con el que se pelea
- Cambiar el tipo de arma
- Bonus de comida, habilidades y objetos
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
  - v0.1.2
    - Se eliminó la carpeta de monstruos y se generó un archivo con todos estos, ademas fueron ingresados al código
  - v0.1.1
    - Se creó una carpeta para monstruos y se comenzó a trabajar con metodos, ademas se hizo una subclase para las espadas y escudos.
  - v0.1.0
    - Se agregaron clases para poder la hacer la calculadora de una forma "bonita" (clases de python) y se dividió el código
  - v0.0.1
    - Version inicial de la calculadora, tan solo se probó la formula para c/c

#Notas:
- Se eliminó la tabla del Daimyo Hermitaur (tambien sub especies), esto se debe a que para una zona existian dos valores (pinzas rotas o no)... quitar esta tabla me simplifica la vid
- Buscando informacion de la defensa de los monstruos me encontré de que en el MHF1 la defensa es variable, pero tambien me encontré que la defensa en offline siempre es 1 y que en online varía, tambien leí que varía según la mision específica, por lo tanto **todos los monstruos serán de rango G** y se supondrá que la defensa es 0.75
- Por el momento los monstruos no tendran estado de ira (haciendo que esta variable sea 1 simpre)

# Problemas actuales:
-
