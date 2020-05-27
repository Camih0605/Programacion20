import sys
import matplotlib.pyplot as plt
import pandas as p
def abrir_archivo(file):
  assert(file)
  return False 
archivo_existe = True 

while(archivo_existe):
  file = input("Ingresa el nombre del archivo: ")
  try :
    archivo_existe = open(file)
    archivo_existe = False
  except FileNotFoundError :
    print("Ingresaste un archivo que no existe")

ppg =p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title(input("Ingrese el titulo de la grafica : "))
plt.xlabel(input("Ingrese el titulo de eje X : "))
plt.ylabel(input("Ingrese el titulo del eje Y : "))
plt.plot(x,y)
#plt.savefig(input("Ingrese el nombre de la grafica : "))
plt.show()


nombre = "\nNo ingresaste el nombre"
try:
    nombre = (input('Ingrese su nombre : '))
except ValueError:
    print ("ingresaste mal el nombre")
print ("Hola", nombre,"procederemos a calcular tu IMC")

edad = "No ingresaste edad"
try:
    edad = int (input('Ingrese su edad : '))
except ValueError:
    print ("ingresaste mal la edad")
print ("Tu edad es", edad)

estatura = "No ingresaste tu estatura"
try:
    estatura = float (input('Ingrese su estatura : '))
except ValueError:
    print ("ingresaste mal la estatura")
print ("Tu estatura es", estatura)

peso = "No ingresaste tu peso"
try:
    peso = float (input('Ingrese su peso : '))
except ValueError:
    print ("ingresaste mal el peso")
print ("Tu peso es", peso)

IMC = ((peso/estatura**2))
print ("Como resultado tu IMC ES : ",IMC)


Pico_ecg= 9

Pico_eeg= 10

pico_ppg= 9

picos= { "Picos": ["ECG", "EEG", "PPG"]}
total= (Pico_ecg,Pico_eeg,pico_ppg)

print(picos["Picos"])
print(total)

plt.bar(picos["Picos"],total)
plt.title("Picos vs Analisis", fontsize=20)
plt.xlabel("Picos")
plt.ylabel("Analisis")
plt.savefig("Picos.png")
plt.show()




#30% Sala , 40% Alcoba , 10% cocina, 10% Balcon 10%Baño
labels = 'Baño', 'Sala', 'Cocina', 'Balcon',"Alcoba",""
sizes = [10, 30, 10, 10, 40]
explode = (0, 0, 0, 0, 0, 0.1) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Porcentajes de lugares de la casa")
plt.savefig("Grafico_casa.png")
plt.show()


################################################

#El aprendiaje supervisado o regresivos son los que necesitan a alguien que es este pendiente
# ya sea colocando los algoritmos para que la maquina funcione correctamente  haga lo que le estan pidiendo
#y en el aprendizaje no supervisado es de inteligencia artificial y la maquina hace el 
#algoritmo sin que se lo digan ya que coge todo lo que tenga relacion y lo aplica
#ejemplo: colores, forma, etc.
