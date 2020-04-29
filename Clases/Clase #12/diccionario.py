diccionario = ()
medios_transporte = ()
medios_transporte ("carros") = ("BMW", "AUDI", "MAZDA", "TOYOTA")
medios_transporte ("motos") = ("AKT", "HONDA", "DSEK")

estudiante_programacion = (
    "Nombres" : ("Daniel", "Valeria", "Camila", "Santiago", "Juanes")
    "Edad" : (11,14,17,12,20)
)

print ("4"+60)
print (estudiante_programacion^^["Edad"] )
print ("4"+60)
print ("Los elementos que componen la llave carros son : {}"
format (medios_transporte  ["carros"] ))

print ("Los elementos que componen la llave motos son : {}"
format (medios_transporte ["motos"] ))

print (medios_transporte.keys ())
print (estudiante_programacion.keys ())
print (list (medios_transporte.keys()))
print (medios_transporte.values())
print (list ( medios_transporte.values ()))
valores = list (medios_transporte.values())
print (valores(0))

