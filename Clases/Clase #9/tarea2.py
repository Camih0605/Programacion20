def  hablar ( mensaje ):
    imprimir ( mensaje )
    return "exitoso"

def  validar_clave ( CLAVE_REAL , _claveIngresada ):
    if ( CLAVE_REAL  ==  _claveIngresada ):
        print ( "ingreso exitoso" )
        ESTADO  =  "Clave valida"
    más :
        print ( "clave incorrecta" )
        ESTADO  =  "Clave invalida"
    volver  ESTADO

def  mostrar_lista ( lista ):
    contador  = 1
    para  elemento  en la  lista :
        print ( contador , "-" , elemento )
        contador  + =  1

def  mostrar_dos_listas ( lista_1 , lista_2, lista_3 ):
    if ( len ( lista_1 ) ==  len ( lista_2 ) == len (  lista_3 )):
        print ( "Doctores" , "Enfermeros" , "Enfermos" )
        para  i  en  rango ( len ( lista_1 )):
            print ( lista_1 [ i ] , lista_2 [ i ] , lista_3 [ i ])

    más :
        print ( "no se puede mostrar uno a uno" )

def  bienvenida (): print ( "Bienvenido al código" )

def  ingrese ():
    intentos  =  0
    estado  =  validar_clave ( 1234 , int ( input ( "ingrese la clave:" )))
    intentos  + =  1
    while ( estado  ! =  "Clave valida"  e  intentos < 3 ):
        estado  =  validar_clave ( 1234 , int ( input ( "ingrese la clave:" )))
        intentos  + =  1
     estado de retorno


bienvenida ()

if  ingresar () ==  "Clave valida" :
    Doctores  = [ "camila" , "pablo" , "hernan" , "Luis" ]
    Enfermeros  = [ "Daniel" , "Samuel" , "Diana" , "Lorena" ]
    Enfermos = [ "Tatiana" , "Fiore" , "Karen" , "Pedro"]
    mostrar_lista ( Doctores )
    mostrar_tres_listas ( Doctores , Enfermeros , Enfermos )
más :
    imprimir ( "Lo sentimos usted no ingreso correctamente, saliendo del programa" )


def  llenarLista ():
    lista  = []
    decicion  =  input ( "ingrese s -> para agregar mas personas n -> para no agregar mas:" )
    while ( decisión  ==  "s" ):
        lista . append ( input ( "ingrese un elemento de la lista:" ))
        decicion  =  input ( "ingres s -> para agregar mas personas n -> para no agregar mas:" )
    volver  lista

print ( "Ingrese la lista de personas" )
Doctores  =  llenarLista ()
print ( "Ingrese la lista de enfermeros" )
Enfermeros  =  llenarLista ()
print ( "Ingrese la lista de enfermos")
Enfermos = llenarLista ()
mostrar_tres_listas ( Doctores , Enfermeros , Enfermos )