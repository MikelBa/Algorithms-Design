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
tiempos=[]
ejex=[]
for x in range(3):
    for y in range(3):
        # inicialización del tablero
        tablero = [[True for j in range(n)] for i in range(n)]
        # llamada al método de backtracking
        t1=time.clock()
        lista = caballo_profundidad((x,y), tablero,[])
        t2=time.clock()
        tiempos.append(t2-t1)
        ejex.append(str((x,y)))

plt.figure()
plt.xlabel("Posiciones(x,y)")
plt.ylabel("Tiempo (segundos)")
plt.xticks(np.arange(9),(ejex))
plt.bar(np.arange(9),tiempos)
plt.show()
