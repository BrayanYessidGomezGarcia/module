import json
#data='{"nombre": "BRAYAN","APELLIDO": "GOMEZ": "Garcia"}'
#convertir= json.loads(data)
#print(convertir)

#diccionario={
    #"nombre": "Brayan",
    #"apellido": "Gomez"
#}
#jsonData= json.dumps(diccionario, ident =4)
#print(jsonData)

convertir= ""
with open("data.json", "r") as f:
    convertir = json.loads(f.read())
    f.close()

with open("data.json", "w") as f:
    convertir = json.loads(f.read())
    convertir["Altura"] = 1.63
    data = json.dumps(convertir, indent=4)
    f.write(data)
    f.close()