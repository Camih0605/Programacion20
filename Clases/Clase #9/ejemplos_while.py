def  hablar ( mensaje ):
    imprimir ( mensaje )
    volver  "exitoso"

def  validar_clave ( CLAVE_REAL , _claveIngresada ):
    if ( CLAVE_REAL  ==  _claveIngresada ):
        imprimir ( "ingreso exitoso" )
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

def  mostrar_dos_listas ( lista_1 , lista_2 ):
    if ( len ( lista_1 ) ==  len ( lista_2 )):
        print ( "elemento" , "precio" )
        for  i  in  range ( len ( lista_1 )):
            print ( lista_1 [ i ], "$" , lista_2 [ i ])

    else :
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
    comidas  = [ "carne" , "pollo" , "huevo" , "Queso" ]
    precios  = [ 12345 , 6789 , 12232 , 4500 ]
    mostrar_lista ( comidas )
    mostrar_dos_listas ( comidas , precios )
más :
    imprimir ( "Lo sentimos usted no ingreso correctamente, saliendo del programa" )


def  llenarLista ():
    lista  = []
    decicion  =  input ( "ingrese s -> para agregar mas elementos n -> para no agregar mas:" )
    while ( decisión  ==  "s" ):
        lista . append ( input ( "ingrese un elemento de la lista:" ))
        decicion  =  input ( "ingres s -> para agregar mas elementos n -> para no agregar mas:" )
    volver  lista

imprimir ( "Ingrese la lista de alimentos" )
comidas  =  llenarLista ()
print ( "Ingrese la lista de precios a esos alimentos" )
precios  =  llenarLista ()
mostrar_dos_listas ( comidas , precios )