listaNombres= ["Camila",
"Daniel",
"Santiago",
"Ysabela",
"Camila2",
"Juanes",
"Elena",
"Fernanda",
"Santiago2",
"David",
"Susana",
"Leslly",
"marco",
"Daniel h"]
listaNombres[0] = "Maria Camila Betancur"
listaNombres[4] = "Maria Camila Mesa"
listaNombres[2] = "Santiago Betancur"
listaNombres[8] = "Santiago Hernandez"
print(listaNombres)
listaNombres.pop(13)
print(listaNombres)
listaNombres.append("Daniel H")
print(listaNombres)

_decision = int (input("""
ingrese: 
1-Para ver lista de nombre
2-Para ver lista de edades
3-Para ver notas
4-Salir"""))
while (_decision!=4):
    if (_decision ==1):
        print(listaNombres)
    elif (_decision ==2):
        print("ListaEdades")
    elif (_decision):
     print("Listanotas")
    else:
     print("Ingrese un valor valido")
    _decision = int (input("""
    ingrese: 
    1-Para ver lista de nombre
    2-Para ver lista de edades
    3-Para ver notas
    4-Salir fsjdkfdj
    : """))





