#-------------MENSAJES-------------------------
PREGUNTA_NOMBRE = "Ingrese su nombre: "
MENSAJE_BIENVENIDO = "Bienvenido al programa"
MENSAJE_DESPEDIDA = "Chao"
MENSAJE_TOCAYO = "Hola hermana somos tocayas"
PREGUNTA_EDAD = "ingrese por favorsito su edad: "
MENSAJE_JOVEN = "Eres jovensita"
MENSAJE_ADULTO = "Eres adulta"
MENSAJE_VIEJO = "Eres viejita linda"
#-------------VARIABLES------------------------
NOMBRE_PERSONAL = "Camila"
#-------------ENTRADAS-------------------------
_nombreUsuario = " "
_edadUsuario = 0 
#-------------CODIGO---------------------------
print(MENSAJE_BIENVENIDO)
_nombreUsuario = input(PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombreUsuario) :
    print(MENSAJE_TOCAYO)
_edadUsuario = int(input(PREGUNTA_EDAD))

if ((_edadUsuario >= 0) and (_edadUsuario <=25 )) :
    print(MENSAJE_JOVEN)
elif ((_edadUsuario >=26 ) and (_edadUsuario <=65)) :
    print(MENSAJE_ADULTO)
else:
    print(MENSAJE_VIEJO)
print(MENSAJE_DESPEDIDA)