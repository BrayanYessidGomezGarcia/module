# from module.camper import
# from module.camper import save
#from module.camper import delate as eliminar
from os import system
import modulos.camper  as camper
import modulos.trainer as trainer 
from modulos.Validate import menuNoValid
def menu():
    print("Sistema de almacenamiento de datos para campus")
    print("\t1. Informacion del camper")
    print("\t2. Informacion del trainer")
    print("\t0. Salir")
bandera=True
while (bandera):
    menu()
    opc = int(input())
    match(opc):
        case 1:
            system("clear")
            camper.menu()
        case 2:
            print("")
        case 0:
            system("clear")
            bandera = False
        case _:
            menuNoValid(opc)