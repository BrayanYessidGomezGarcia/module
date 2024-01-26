from os import system
from .data import camper
from .Validate import menuNoValid

def save(nombre):
   camper.append(nombre)
   return f"Succesfully Camper"
def edit():
   return "Edit to trainer"
def search():
   return "The trainer is available"
def delate():
   return "Trainer delated"
def menu():
 
 bandera= True
 while (bandera):
    print("CRUD del camper")
    print("\t1. Guardar camper")
    print("\t2. Guardar camper")
    print("\t3. Guardar camper")
    print("\t4. Eliminar camper")
    print("\t0. Atras")

opc= int(input())
match(opc):
    case 1:
        save()
    case 0:
        system("clear")
        bandera= False
    case _:
        print("")