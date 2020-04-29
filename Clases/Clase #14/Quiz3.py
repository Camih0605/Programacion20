import pandas as p
diccionario =p.read_csv("barrios.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict
print(diccionario)
print(diccionario.keys())
print(diccionario["Barrio"])

mayor_nombre = max (diccionario["Barrio"].values(), key=len)
menor_nombre = min (diccionario["Barrio"].values(), key=len)

print("El barrio con el nombre mas largo es {} y el nombre mas corto es {}".format(mayor_nombre,menor_nombre))


con_maxiagua = max (diccionario["Agua"].values())
con_minagua = min (diccionario["Agua"].values())
print ("El maximo consumo de agua es {} y el minimo consumo de agua es {}".format(con_maxiagua,con_minagua))

con_maxiener = max (diccionario["Energía"].values())
con_minener = min (diccionario["Energía"].values())
print ("El maximo consumo de energía es {} y el minimo consumo de energía es {}".format(con_maxiener,con_minener))

con_maxigas = max (diccionario["Gas"].values())
con_mingas = min (diccionario["Gas"].values())
print ("El maximo consumo de gas es {} y el minimo consumo de gas es {}".format(con_maxigas,con_mingas))

con_maxinter = max (diccionario["Internet"].values())
con_mininter = min (diccionario["Internet"].values())
print ("El maximo consumo de internet es {} y el minimo consumo de internet es {}".format(con_maxinter,con_mininter))

can_maxhabi = max (diccionario["Habitantes"].values())
can_minhabi = min (diccionario["Habitantes"].values())
print ("La cantidad maxima de habitantes es {} y la cantidad minima de habitantes es {}".format(can_maxhabi,can_minhabi))





