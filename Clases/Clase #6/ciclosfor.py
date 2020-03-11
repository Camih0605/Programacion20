# _cantidadSaltos = int (input("Ingrese la cantidad de saltos : "))
# for i in range(4):
#     print(i)

# for i in range (_cantidadSaltos):
#     print("El canguro da su salto numero",i+1)

# DIAS = ("lunes", "martes", "miercoles", "jueves", "viernes" )
# for dia in DIAS :
#     print(dia)

NOMBRES = ["Camilo", "Felipe", "Sara", "Dary", "Emilio", "Bruno"]
EDADES = [14,18,2,25,18,19]
print(len(NOMBRES), len(EDADES))
for i in range (len(NOMBRES)):
    if EDADES[i] >= 18 :
        print(i, "LA PERSONAS" ,NOMBRES[i], "ES MAYOR")

sumaEdades =0
for edad in EDADES:
    sumaEdades = sumaEdades + edad
print(sumaEdades)







