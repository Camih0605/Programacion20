#numero = 0
#NUMERO_DESEADO = 12
#while(numero <= NUMERO_DESEADO):
    #numero = numero +1
    #print(numero)
#print(numero)

#NUMERO FAVORITO
import random
PREGUNTA_NUMERO = "Ingrese un numero entero 1-10: "
NUMERO_FAVORITO = random.randint(1,10)
MENSAJE_FALLO = "FALLASTE!! INTENTALO DE NUEVO"
MENSAJE_ACIERTO = "FELICIDADES, SABES MI NUMERO FAVORITO"
MENSAJE_MAYOR= "Estas cerca el numero que ingreso es mas grande"
MENSAJE_MENOR= "Estas cerca el numero que ingreso es mas menor"
_numeroIngresado = int(input(PREGUNTA_NUMERO))
while(_numeroIngresado != NUMERO_FAVORITO):
    print(MENSAJE_FALLO)
    if (_numeroIngresado>NUMERO_FAVORITO):
          print(MENSAJE_MAYOR)
    else: print(MENSAJE_MENOR)
    _numeroIngresado = int(input(PREGUNTA_NUMERO))
print (MENSAJE_ACIERTO)