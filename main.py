# from module.camper import
# from module.camper import save
#from module.camper import delate as eliminar
import Modulos.camper  as camper
import Modulos.trainer as trainer 
from os import system
bandera= True
while(bandera): 
 print("Sistema de almacenamiento de datos para campus")
 print("\t1. Informacion del camper")
 print("\t2. Informacion del camper")
 print("\t0. Salir")


opc= int(input())

match(opc):
    case 1:
        system("clear")
        camper.menu()
        opc= int (input())
    case 2: 
        print("")
    case _:
        print("")
