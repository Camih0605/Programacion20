
import random

DADO1 = 1
DADO2 = 1
SUMA = 2
NUMERO_DESEADO = 12

while(SUMA != NUMERO_DESEADO ):
    print(SUMA)
    DADO1 = random.randint(1,6)
    DADO2 = random.randint(1,6)
    SUMA = DADO1 + DADO2
print (SUMA)