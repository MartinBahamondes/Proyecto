import os

def menu():
    os.system("cls")
    print("Bienvenid@!")
    print ("Seleccione una Opcion")
    print ("1-Consultar una región por su nombre\n2-Busqueda de datos de una región mediante su codigo\n3-Región con más y menos contagios con síntomas\n4-Salir")

def opcion_menu(val1,val2):
    while True:
        try:
            opcion=int(input("Ingrese una opcion: "))
            if(opcion>=val1 and opcion <= val2):
                valsalida=opcion
                break
            else:
                print("Ingrese una opcion valida")
        except:
            print("Ingrese una opcion valida")
    return(valsalida)

def tabla():
    print(".-------------------------------------------------------------------------.")
    print("|                          Regiones disponibles                           | ")
    print(".-------------------------------------------------------------------------.")
    print("| Arica y Parinacota | Tarapacá      | Antofagasta | Atacama | Coquimbo   |")
    print("| Valparaíso         | Metropolitana | O’Higgins   | Maule   |  Ñuble     |")
    print("| Biobío | Araucanía |Los Ríos       | Los Lagos   |  Aysén  | Magallanes |")
    print(".-------------------------------------------------------------------------.")