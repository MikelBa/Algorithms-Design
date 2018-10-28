import time
import matplotlib.pyplot as plt
import numpy as np

def posiciones_factibles(casilla,tablero):
    n=len(tablero)
    i,j = casilla
    l=[]
    for di,dj in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]:
        if 0<=i+di<n and 0<=j+dj<n and tablero[i+di][j+dj]:
            l.append((i+di,j+dj))
    return l

def caballo_profundidad(pos_in, tablero, sol_parc):
    global nodos
    nodos+=1
    n=len(tablero)
    soluciones=[]
    sol_parc.append(pos_in)
    i,j=pos_in
    tablero[i][j]=False
    if len(sol_parc)==n*n:
        soluciones=soluciones+sol_parc
    else:
        for move in posiciones_factibles(pos_in,tablero):
            soluciones.extend(caballo_profundidad(move,tablero,sol_parc))
    del sol_parc[-1]
    tablero[i][j]=True
    return soluciones

#### PROGRAMA PRINCIPAL ####

n=int(input('Tamaño del tablero: '))
print("\nGráficos cambiando posiciones de búsqueda en profundidad")
cantnodos=[]
ejex=[]
for x in range(3):
    for y in range(3):
        # inicialización del tablero
        tablero = [[True for j in range(n)] for i in range(n)]
        nodos=0
        # llamada al método de backtracking
        lista = caballo_profundidad((x,y), tablero,[])
        cantnodos.append(nodos)
        ejex.append(str((x,y)))

plt.figure()
plt.xlabel("Posiciones(x,y)")
plt.ylabel("Nodos explorados")
plt.xticks(np.arange(9),(ejex))
plt.bar(np.arange(9),cantnodos)
plt.show()
