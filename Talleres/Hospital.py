#----------------------------MENSAJES----------
PREGUNTA_PACIENTES = "Ingrese el numero de pacientes: "
MENSAJE_RIESGOBAJO = "El riesgo es bajo"
MENSAJE_RIESGOMEDIO = "El riesgo es medio"
MENSAJE_RIESGOALTO = "El riesgo es alto"
PREGUNTA_UCI = "Ingrese el numero de pacientes en la UCI: "
#-----------------VARIABLES----------------------
#-----------------ENTRADAS-----------------------
_numeroPacientes = 0
_numeroPacientesuci = 0
#------------------CODIGO------------------------
_numeroPacientes = int(input(PREGUNTA_PACIENTES))
if ((_numeroPacientes>0) and (_numeroPacientes<=1000)):
    print(MENSAJE_RIESGOBAJO)
elif((_numeroPacientes>1001) and (_numeroPacientes<5000)):
    print(MENSAJE_RIESGOMEDIO)
else:
    print(MENSAJE_RIESGOALTO)   
_numeroPacientesuci = int(input(PREGUNTA_UCI))
if (_numeroPacientesuci>1000):
    print(MENSAJE_RIESGOALTO)
elif((_numeroPacientesuci<=1000)):
    print(MENSAJE_RIESGOMEDIO)
 

