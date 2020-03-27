MENSAJE_BIENVENIDO= "bienvenido al programa" 

#--------------Codigo-------------

print (MENSAJE_BIENVENIDO) 

pesosPacientesIniciales = [32,64,74,85,98,115,122,127,137,148]  


def mostrar_lista (pesosPacientesIniciales):
    if (len(pesosPacientesIniciales)):
        for i in range(len(pesosPacientesIniciales)): 
            print (pesosPacientesIniciales[i])


mostrar_lista(pesosPacientesIniciales)

presiones= []
for peso in pesosPacientesIniciales: 
    presiones.append(peso*6)

def llenarLista (): 
    pesoPaciente = []
    decision = int(input(""" Ingrese: 
          1 - para añadir peso
          2 - finalizar
          """))
    while(decision == "1"):
        pesoPaciente.append (input("ingrese el peso nuevo: "))
        decision = int(input("""
        Ingrese: 
          1 - para añadir peso
          2 - finalizar
          """))
    return pesoPaciente
llenarLista() 

print (pesoPaciente , presiones)


#encontrar la presion más grande de la lista
print ("la presion mas grande en la lista {} es el {}".format(lista,max (presiones)))

#encontrar la presion más pequeña de la lista
print ("la presion mas pequeña en la lista {} es el {}".format(lista,min (presiones)))

#decreciente
presion.sort(reverse=True)
print ("lista ordenada decrecientemente {}".format(presiones))


#tamaño de una lista
print ("la lista {} tiene un tamaño de {} pacientes".format(lista ,len (presiones)))



