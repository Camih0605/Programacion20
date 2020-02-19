PREGUNTA_NOMBRE= "Ingrese su nombre: "
MENSAJE_BIENVENIDO= "Bienvenido"
MENSAJE_PROGRAMA= "a este programa"
PREGUNTA_EDAD= "Ingrese su edad: "
MENSAJE_EDAD= "Tu edad es: "
PREGUNTA_ESTATURA= "Ingrese tu estatura: "
MENSAJE_ESTATURA= "Tu estatura es: "
MENSAJE_DESPEDIDA= "Chao"
_nombrePersona= input(PREGUNTA_NOMBRE)
print(PREGUNTA_NOMBRE,_nombrePersona,MENSAJE_BIENVENIDO)
_edadPersona=int(input(PREGUNTA_EDAD))
print(MENSAJE_EDAD,_edadPersona)
print (type(_edadPersona))
_estaturaPersona=float(input(PREGUNTA_ESTATURA))
print(MENSAJE_ESTATURA,_estaturaPersona)
print (type(_estaturaPersona))
print (MENSAJE_DESPEDIDA)
