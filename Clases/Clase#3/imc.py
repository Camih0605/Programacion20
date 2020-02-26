#-------------MENSAJES-------------------------
PREGUNTA_NOMBRE = "Ingrese su nombre: "
MENSAJE_BIENVENIDO = "Bienvenido al programa"
MENSAJE_DESPEDIDA = "Chao"
MENSAJE_TOCAYO = "Hola hermana somos tocayas"
PREGUNTA_PESO = "Ingrese su peso en kg: "
PREGUNTA_ESTATURA = "Ingrese su estatura en metros: "
MENSAJE_FLACO = "Cuida tu salud, tu imc es bajo"
MENSAJE_SALUDABLE = "Tienes un peso saludable"
MENSAJE_SOBREPESO = "Cuida tu salud, estas en sobrepeso"
MENSAJE_OBESIDAD = "Cuida tu salud, tienes obesidad"
#-----------------VARIABLES----------------------
NOMBRE_PERSONAL= "Camila"
IMC= 0.0
#---------------------ENTRADAS--------------------
_nombreUsuario = " "
_pesoUsuario = 0.0
_estaturaUsuario = 0.0 
#-------------------CODIGO-------------------------
print(MENSAJE_BIENVENIDO)
_nombreUsuario = input(PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombreUsuario) :
    print(MENSAJE_TOCAYO)
_pesoUsuario = float (input(PREGUNTA_PESO))
_estaturaUsuario = float (input(PREGUNTA_ESTATURA))
IMC = ((_pesoUsuario/_estaturaUsuario**2))
print (IMC)
if ((IMC >= 12) and (IMC<=18)):
    print (MENSAJE_FLACO)
elif ((IMC >=19) and (IMC <=24)):
    print (MENSAJE_SALUDABLE)
elif ((IMC >=30) and (IMC <=39)):
    print (MENSAJE_SOBREPESO)
else:
    print(MENSAJE_OBESIDAD)
print(MENSAJE_DESPEDIDA)