import funciones_lectura_archivos as helper
##Leimos el archivo
lineas= helper.leer_archivo("noticia.txt")
#Lo mostramos linea por linea
helper.mostrar_lineas(lineas)

archivo = open"("noticia.txt",'a')
archivo.write= ("\nRevista: el español")
archivo.close()
helper.escritura_archivo("noticia.txt",Texto)
helper.agregar_lineas_archivo("opinion.txt","\n14 de Febrero 2020")