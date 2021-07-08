#Importar librerias
import os
import numpy as np
import matplotlib.pyplot as plt
import funciones as fn
#Limpiador de pantalla
os.system("cls")



#Grafico de barras
#x=[1,1,1,2,2,3]
#plt.hist(x)
#plt.show()

#                   0                      1                     2                     3                4            5           6            7              8              9            10        11          12         13          14          15           16            17            18              19               20              21              22           23           24          25           26           27          28           29           30        31        32      33       34       35       36       37        38        39         40           41           42           43          44          45         46          47           48           49          50          51      52        53         54          55              56
regiones = ["ARICA Y PARINACOTA", "Arica y Parinatoca", "Arica y parinacota", "arica y parinacota", "TARAPACA", "Tarapaca", "tarapaca", "ANTOFAGASTA", "Antofagasta", "antofagasta", "ATACAMA", "Atacama", "atacama", "COQUIMBO", "Coquimbo", "coquimbo", "VALPARAISO", "Valparaiso", "valparaiso", "METROPOLITANA", "Metropolitana", "metropolitana", "O'HIGGINS", ",O HIGGINS", "OHIGGINS", "O'higgins", "O Higgins", "OHiggins", "o’higgins", "o higgins", "ohiggins", "MAULE", "Maule", "maule", "ÑUBLE", "Ñuble", "ñuble", "BIOBIO", "Biobio," "biobio", "ARAUCANIA", "Araucania", "araucania", "LOS RIOS", "Los Rios", "Los rios", "los rios", "LOS LAGOS", "Los Lagos", "Los lagos", "los lagos", "AYSEN", "Aysen", "aysen", "MAGALLANES", "Magallanes", "magallanes"]
regiones1 = ["Arica y Parinacota","Tarapaca","Antofagasta","Atacama","Coquimbo","Valparaiso","Metropolitana","O'Higgins", "O Higgins","Maule","Ñuble","Biobio","Araucania","Los Rios","Los Lagos","Aysen","Magallanes"]

#Menu
while True:
    fn.menu()
    opcion=fn.opcion_menu(1,4)
    if(opcion==1):
        os.system("cls")
        fn.tabla()
        regionselec = input("Escriba la región a consultar respetando las mayusculas y sin acentos aqui → ")
        while not regionselec in regiones1:
            print("Región incorrecta, intente nuevamente")
            input("Presione cualquier tecla para intentar nuevamente")
            break
        else:
            print("Región ingresada correctamente")
            if regionselec == regiones1[0]:
                x=[1,1,1,2,2,3]
                plt.title("Arica y Parinacota")
                plt.hist(x)
                plt.show()
            else:
                if regionselec == regiones1[1]:
                    x=[1,1,1,2,2,3]
                    plt.hist(x)
                    plt.show()
                else:
                    if regionselec == regiones1[2]:
                        x=[1,1,1,2,2,3]
                        plt.hist(x)
                        plt.show()
                    else: 
                        if regionselec == regiones1[3]:
                            x=[1,1,1,2,2,3]
                            plt.hist(x)
                            plt.show()
                    break
    elif(opcion==2):
        os.system("cls")
        input("Ingrese el codigo de la region por la que quiere consultar → ")
        break
    elif(opcion==3):
        os.system("cls")
        break
    elif(opcion==4):
        os.system("cls")
        break
    else:
        os.system("cls")
        print("---Ingrese una opcion valida---")