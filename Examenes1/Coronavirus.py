#----------------------------MENSAJES----------
PREGUNTA_TEMPERATURA = "Ingrese su temperatura: "
MENSAJE_SALUDABLE = "Estado Saludable"
MENSAJE_HIPOTERMIA = "Estado Hipoermia"
MENSAJE_ALERTA = "Estado alerta"
MENSAJE_PELIGRO = "Estado peligro"
PREGUNTA_PAIS = "Ingrese el lugar de donde viene: "
MENSAJE_BIENVENIDO = "Bienvenido al programa"
MENSAJE_DESPEDIDA = "Chao"
MENSAJE_OBSERVACION = "Estado de observacion"
#----------------------VARIABLES--------------
LUGAR_PAISES = ["China", "Iran", "Italia"]
#----------------------------ENTRADAS----------
_temperaturaPacientes= 0.0
_nombrePais = " "

#---------------CODIGO-------------------------
print(MENSAJE_BIENVENIDO)
_nombrePais = input (PREGUNTA_PAIS)
if (_nombrePais in LUGAR_PAISES) :
    print(MENSAJE_OBSERVACION)
_temperaturaPacientes = int(input(PREGUNTA_TEMPERATURA))
if ((_temperaturaPacientes>36) and (_temperaturaPacientes<=38.4)) :
    print(MENSAJE_SALUDABLE)
elif((_temperaturaPacientes<36)) :
    print(MENSAJE_HIPOTERMIA)
elif((_temperaturaPacientes>38.5) and (_temperaturaPacientes<40)) :
    print(MENSAJE_ALERTA)
else:
    print(MENSAJE_PELIGRO)

print(MENSAJE_DESPEDIDA)





