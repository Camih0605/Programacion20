class Canguros():
    def _init_(self, raza ,identificacion ,edad):
        self.raza = raza
        self.identificacion = identificacion 
        self.edad = edad
    def saltar(self, CantidadSaltos):
        for i in range (CantidadSaltos):
            print ("Salto ", i+1)
        

canguro1 = Canguro("Rojo",1,15)
canguro1.saltar(12)
canguro2 = Canguro("Gris oriental",2,12)
canguro3 = Canguro("Antilopine"3,10)
canguro4 = Canguro("Rojo",4,13)
canguro5 = Canguro("Gris occidental",5,9)
canguro6 = Canguro("Antilopine",6,8)
canguro7 = Canguro("Rojo",7,21)
canguro8 = Canguro("Rojo",8,19)
canguro9 = Canguro("Gris Oriental",9,25)
canguro10 = Canguro("Rojo",10,4)

print ("La raza del primer canguro es", canguro1.raza)

class Cuidadores():
    def _init_(self, id, nombre):
        self.id = id
        self.nombre = nombre
    def alimentar_canguros(self,canguros):
         print ("Voy alimentar a los canguros")
         size = canguros
         return size

class Jefe(Cuidadores),cuidador2:
    def contratar_cuidador(self, id, nombre):
        print("procedo a contratar cuidador")
        contratar = Cuidador3
        return Cuidador


Cuidador1 = Cuidador(34,"Camila")
Cuidador2 = Cuidador(37,"Andres")
Cuidador3 = Cuidador(39,"Juan")
Cuidador4 = Cuidador(30,"Diana")
Cuidador5 = Cuidador(45,"Jonatan")

canguros= 94
Comida = Cuidador1.alimentar_canguros(canguros)
print ("Hola a todos soy", Cuidador1.nombre, "y voy alimentar a", canguros, "canguros")

Cuidador2 = Jefe(37,"Andres")
print("Hola a todos voy a contratar un nuevo cuidador llamado", Cuidador3.nombre)


