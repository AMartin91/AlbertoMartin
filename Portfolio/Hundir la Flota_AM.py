
import numpy as np
import pandas as pd

#Bienvenida al juego

def menu():

    mensaje_inicial ="""

██╗  ██╗██╗   ██╗███╗   ██╗██████╗ ██╗██████╗     ██╗      █████╗     ███████╗██╗      ██████╗ ████████╗ █████╗ 
██║  ██║██║   ██║████╗  ██║██╔══██╗██║██╔══██╗    ██║     ██╔══██╗    ██╔════╝██║     ██╔═══██╗╚══██╔══╝██╔══██╗
███████║██║   ██║██╔██╗ ██║██║  ██║██║██████╔╝    ██║     ███████║    █████╗  ██║     ██║   ██║   ██║   ███████║
██╔══██║██║   ██║██║╚██╗██║██║  ██║██║██╔══██╗    ██║     ██╔══██║    ██╔══╝  ██║     ██║   ██║   ██║   ██╔══██║
██║  ██║╚██████╔╝██║ ╚████║██████╔╝██║██║  ██║    ███████╗██║  ██║    ██║     ███████╗╚██████╔╝   ██║   ██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝

                Bienvenido a la batalla naval interectiva, ¿Dispuesto a derrotar a tu rival?

            Inserta A para Jugar
            Inserta Z para salir
                                                                                                                                                                                                                                             
"""
    print(mensaje_inicial)
    opciones()

#Funcion para entrar a jugar o salir del juego

def opciones():

    opcion = (input("Inserta option: A para jugar o Z para salir"))
    if opcion == "A":
        crear_mapa()
        barcos()
        turno_persona()

    elif opcion == "Z":
        print("¡Gracias por usar el programa!")
    else:
        print("Solo acepta A y Z: ")
        opciones()

#Creación de los tableros de juego

def crear_mapa():
    """
    Funcion para crear los mapas
    mapa1 y mapa2 serán los mapas visibles sin los barcos para mostrar al jugador
    mapa3 y mapa4 serán los mapas no visibles donde estarán los barcos colocados 
    """
    global mapa1
    mapa1 = list("≈")*100
    mapa1 = np.array(mapa1).reshape(10,10)
    
    global mapa2
    mapa2 = list("≈")*100
    mapa2 = np.array(mapa2).reshape(10,10)

    global mapa3
    mapa3 = list("≈")*100
    mapa3 = np.array(mapa3).reshape(10,10)
    
    global mapa4
    mapa4 = list("≈")*100
    mapa4 = np.array(mapa4).reshape(10,10)

#Posicionamiento de los barcos

def barcos():
    global i
    global eslora
    for i in mapa3, mapa4:
        eslora = 1
        numero_barcos = 4
        inicial = 4
        while eslora < 5:
            if eslora == 1:
                x = np.random.randint(0, 10)
                y = np.random.randint(0, 10)
                if numero_barcos == 1:
                    barco_pequeño()
                    numero_barcos = inicial - eslora
                    eslora +=1
                else:
                    barco_pequeño()
                    numero_barcos -=1
            elif eslora != 1:
                if numero_barcos == 1:
                    barco_grande()
                    numero_barcos = inicial - eslora
                    eslora +=1
                else:
                    barco_grande()
                    numero_barcos -=1

def barco_pequeño():
        x = np.random.randint(0, 10)
        y = np.random.randint(0, 10)
        if i[x,y] != "≈":
            pass
        else:
            i[x,y] = "O"

def barco_grande():
        posicion = np.random.randint(0, 2)
        if posicion == 0: #horizontal
            x = np.random.randint(0, 10)
            y = np.random.randint(0, 10-(eslora-1))
            z = y + eslora
            if "O" in i[x,y:z]:
                pass
            else:
                i[x,y:z] = "O"
        elif posicion == 1: #vertical
            x = np.random.randint(0, (eslora-1))
            y = np.random.randint(0, 10)
            z = x + eslora
            if "O" in i[x:z,y]:
                pass
            else:
                i[x:z,y] = "O"

#Juego, turno manual

def turno_persona():
    j = 1
    while True:
        if np.count_nonzero(mapa4 == "O") == 0:
            ganar()
            break
        elif np.count_nonzero(mapa3 == "O") == 0:
            print("Lo siento, no te quedan más barcos")
            break
        else:
            imprime_mapa()
            ABC = input("Coordenada x o Z para salir")
            if ABC == "Z":
                print("¡Gracias por usar el programa!")
                break
            diccionario = {"A": 0, "B": 1, "C": 2, "D":3, "E": 4, "F":5, "G": 6, "H":7 , "I": 8, "J":9}
            xu = input("Coordenada y")
            yu = diccionario.get(ABC)
            try:
                if mapa4[int(xu),yu] == "≈":
                    mapa4[int(xu),yu] = " "
                    mapa2[int(xu),yu] = " "
                    print("AGUA")
                    turno_ordenador()
                    j += 1
                    print(f'[ Ronda {j} ]')
                elif mapa4[int(xu),yu] == "O":
                    mapa4[int(xu),yu] = "X"
                    mapa2[int(xu),yu] = "X"
                    print("TOCADO")
                    turno_persona()
                    j += 1
                    print(f'[ Ronda {j} ]')
                else:
                    print("Selecciona una coordenada no seleccionada antes")
                    pass
            except (IndexError, ValueError):
                print("""
        Introduzca solo un valor por coordenada:
        
        Coordenada x: Valores estre A y J
        Coordenada y: Valores entre 0 y 9
        
        """)
                continue

#Juego, turno máquina

def turno_ordenador():
# turno ordenador
    xi = np.random.randint(0, 10)
    yi = np.random.randint(0, 10)
    if mapa3[xi,yi] == "≈":
        mapa3[xi,yi] = " "
        mapa1[xi,yi] = " "
        print("CPU AGUA")
    elif mapa3[xi,yi] == "O":
        mapa3[xi,yi] = "X"
        mapa1[xi,yi] = "X"
        print("CPU TOCADO")
        turno_ordenador()
    else:
        pass

#Juego, imprimir mapa para el usuario

def imprime_mapa():
    print(pd.concat([d.reset_index(drop=True)for d in [
        pd.DataFrame(mapa1, columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]), 
        pd.DataFrame(mapa2, columns=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])]],
        keys= ["Tu", "Enemigo"], join="inner",axis=1))

#Mensaje para el ganador del juego

def ganar():

    mensaje_ganador ="""
   ______                                   __       
  / ____/  ____ _   ____   ____ _   _____  / /_  ___ 
 / / __   / __ `/  / __ \ / __ `/  / ___/ / __/ / _\\
/ /_/ /  / /_/ /  / / / // /_/ /  (__  ) / /_  /  __/
\____/   \__,_/  /_/ /_/ \__,_/  /____/  \__/  \___/ 
                                                     
            Has hundido todos los barcos
                                                                                                                                                                                                                                             
"""
    print(mensaje_ganador)

menu()

