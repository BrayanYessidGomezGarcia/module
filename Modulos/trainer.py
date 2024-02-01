import json
from os import system
from .validate import menuNoValid
from .data import trainer, generos
def save():
    info = {
        "Nombre": input("Ingrese el nombre del trainer\n"),
        "Apellido": input("Ingrese el apellido del trainer\n"),
        "Edad": int(input("Ingrese la edad del trainer\n")),
        "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
    }
    trainer.append(info)
    with open("module/storage/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Trainer"
def edit():
    while(True):
            system('clear')
            print("""
        ****************************
        * Actualizacion del trainer *
        ****************************
        """)
            codigo = ((input('Ingrese el codigo del trainer que desea actualilzar:\n'))-1)
            print(f"""
        ________________________
        Codigo: {codigo+1}
        Nombre: {trainer[codigo].get('Nombre')}
        Apellido: {trainer[codigo].get('Apellido')}
        Edad: {trainer[codigo].get('Edad')}
        Genero: {trainer[codigo].get('Genero')}
        ________________________
        """)    
            print('Este es el trainer que desea actualizar?\n')
            print('1. Si')
            print('2. No')
            print('3. Salir')
            opc = (input())
            if not opc.isnumeric:
                break
            elif(opc == 1):
                info = {
                    "Nombre": input("Ingrese el nombre del trainer\n"),
                    "Apellido": input("Ingrese el apellido del trainer\n"),
                    "Edad": int(input("Ingrese la edad del trainer\n")),
                    "Genero": input("Elija su genero:\n\t"+"\t".join([f"{generos.index(i)+1}. {i}\n" for i in sorted(generos)]))
                    }
                trainer[codigo] = info
                with open("module/storage/trainer.json", "w") as f:
                    data = json.dumps(trainer, indent=4)
                    f.write(data)
                    f.close()
                    break
            elif opc == 3:
                break
    return "Edit to trainer"
def search():
    system('clear')
    print("""
    ********************
    * Lista de trainers *
    ********************
    """)
    for i,val in enumerate(trainer):
        print(f"""
________________________
Codigo: {i+1}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Edad: {val.get('Edad')}
Genero: {val.get('Genero')}
________________________
""")
    return "The trainer is available"
def delete():
    while(True):
            system('clear')
            print("""
        **************************
        * Eliminacion de trainer *
        **************************
        """)
            codigo = (int(input('Ingrese el codigo del trainer que desea eliminar:\n'))-1)
            print(f"""
        ________________________
        Codigo: {codigo+1}
        Nombre: {trainer[codigo].get('Nombre')}
        Apellido: {trainer[codigo].get('Apellido')}
        Edad: {trainer[codigo].get('Edad')}
        Genero: {trainer[codigo].get('Genero')}
        ________________________
        """)    
            print('Este es el trainer que desea actualizar?\n')
            print('1. Si')
            print('2. No')
            print('3. Salir')
            opc = int(input())
            if(opc == 1):
                trainer.pop(codigo)
                with open("module/storage/trainer.json", "w") as f:
                    data = json.dumps(trainer, indent=4)
                    f.write(data)
                    f.close()
                    break
            elif opc == 3:
                break
    return "Trainer deleted"
def menu():
    while (True):
        print("CRUD del trainer")
        print("\t1. Guardar trainer")
        print("\t2. Buscar trainer")
        print("\t3. Actualizar trainer")
        print("\t4. Eliminar trainer")
        print("\t0. Atras")
        opc = int(input())
        if not opc.isnumeric():
            menuNoValid(opc)
        match(opc):
            case '1': save()
            case '2': search()
            case '3': edit()
            case '4': delete()
            case '0':
                system("clear")
                break
            case _: 
                if not opc.isnumeric():
                    break
                menuNoValid(opc)
