import pandas as p
diccionario =p.read_csv("balance.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict
print(diccionario)
print(diccionario.keys())
print(diccionario["Ciudad"])

mayor_nombre = max (diccionario["Cuidad"].values(), key=len)
menor_nombre = min (diccionario["Ciudad"].values(), key=len)

print("La Ciudad con el nombre mas largo es {} y el nombre mas corto es {}".format(mayor_nombre,menor_nombre))


mont_ganan = max (diccionario["Ganancias"].values())
mont_perdi = max (diccionario["Perdidas"].values())
print ("El mayor monto de ganancias {} y el mayor monto de perdidas {}".format(mont_ganan,mont_perdi))



