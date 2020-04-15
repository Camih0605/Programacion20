MENSAJESVALIDO= "Ingrese un numero valido"
class Estudiantes():
    def _init_(self,nombre ,edad ,genero, bachiller):
        self.nombre = nombre
        self.edad = edad 
        self.genero = genero
        self.bachiller = bachiller
    def asistir_aclases(self, Clases):
        for i in range (Clases):
            print ("Soy {} y asistí a {} clases y sé contar muy bien jaj".format(self.nombre, i+1))

Estudiante1 = Estudiante("Camila",18,"Femenino","San fernando")
Estudiante1.asistir_aclases(10)
Estudiante2 = Eatudiante("Sofia",20,"Femenino","Normal")
Estudiante2.asistir_aclases(8)
Estudiante3 = Estudiante("Jonatan",22,"Masculino","Maria auxiliadora")
Estudiante3.asistir_aclases(9)
Estudiante4 = Estudiante("Juan Jose",20,"Masculino","Ferrini")
Estudiante4.asistir_aclases(13)
Estudiante5 = Estudiante("Magdalena",21,"Femenino","Normal")
Estudiante5.asistir_aclases(4)

class Profesores():
    def _init_(self, nombre, edad, niveleducativo):
        self.nombre = nombre
        self.edad = edad
        self.niveleducativo = niveleducativo
    def dictar_clase(self, Clasesdic):
        for i in range (Clasesdic):
            print ("Soy el profesor{} y dicté {} clases y sé contar muy bien jaj".format(self.nombre, i+1))



class Director(Profesores), Profesor2:
    def contratar_profesor(self, nombre, edad, niveleducativo):
        print("procedo a contratar 2 profesores")
        contratar = Profesor3, profesor4
        return Profesor


Profesor1 = Profesor("Carolina",38,"Nivel3")
Profesor1.dictar_clase(9)
Profesor2 = Profesor("Andres",45,"Nivel8")
Profesor3 = Profesor("Juan Carlos",30,"Nivel2")
Profesor3.dictar_clase(15)
Profesor4 = Profesor("Diana",40,"Nivel5")
Profesor4.dictar_clase(11)
Profesor5 = Profesor("Julian",39,"Nivel3")
Profesor5.dictar_clase(10)



Profesor2 = Director("Andres",45,"Nivel8")
Director = Director("Andres",45,"Nivel8")
print("Hola a todos voy a contratar a un profesor llamado", Profesor3.nombre)
print("Hola a todos voy a contratar otro profesor llamado", Profesor4.nombre)


_opcion= int(input("""

    1.Mostrar los atributos de los estudiantes

    2.Mostrar los atributos de los profesores

    3.Mostrar los atributos del director

    4.salir

"""))
while (_opcion !=4 ):
    if (_opcion == 1):
        

         print(Estudiante1.nombre, Estudiante1.edad, Estudiante1.genero, Estudiante1.bachiller)

    

         print(Estudiante2.nombre, Estudiante2.edad, Estudiante2.genero, Estudiante2.bachiller)

    

         print(Estudiante3.nombre, Estudiante3.edad, Estudiante3.genero, Estudiante3.bachiller)
        
        

         print(Estudiante4.nombre, Estudiante4.edad, Estudiante4.genero, Estudiante4.bachiller)

        

         print(Estudiante5.nombre, Estudiante5.edad, Estudiante5.genero, Estudiante5.bachiller)

    elif (_opcion ==2):

         print(Profesor1.nombre, Profesor1.edad, Profesor1.niveleducativo)

        


         print(Profesor2.nombre, Profesor2.edad, Profesor2.niveleducativo)

        

         print(Profesor3.nombre, Profesor3.edad, Profesor3.niveleducativo)
        
        

         print(Profesor4.nombre, Profesor4.edad, Profesor4.niveleducativo)

        

         print(Profesor5.nombre, Profesor5.edad, Profesor5.niveleducativo)

    elif(_opcion ==3):   

         print(Director.nombre, Director.edad, Director.niveleducativo)

    else:

        print(MENSAJESVALIDO)
    
    _opcion= int(input("""

     1.Mostrar los atributos de los estudiantes

     2.Mostrar los atributos de los profesores

     3.Mostrar los atributos del director

     4.salir

    """))
 

        

    

        



