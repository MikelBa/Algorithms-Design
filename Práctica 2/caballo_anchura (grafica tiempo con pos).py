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

def caballo_anchura(pos_in, tablero):
    n=len(tablero)
    i,j=pos_in
    tablero[i][j]=False
    V=[[pos_in,tablero,[pos_in]]]
    soluciones=[]
    while len(V)!=0:
        if len(V[0][2])!=n*n:
            t=V[0][1]
            recorrido=V[0][2]
            for move in posiciones_factibles(V[0][0],t):
                i,j=move
                fila=t[i][:]
                fila[j]=False
                t[i]=fila
                nuevo_recorrido=recorrido+[move]
                V.append([move,t[:][:],nuevo_recorrido])
                fila=t[i][:]
                fila[j]=True
                t[i]=fila
            del V[0]
        else:
            soluciones.append(V[0][2])
            del V[0]
    return soluciones
        
    


#### PROGRAMA PRINCIPAL ####

n=int(input('Tamaño del tablero: '))
print("\nGráficos cambiando posiciones de búsqueda en anchura")
tiempos=[]
ejex=[]
for x in range(3):
    for y in range(3):
        # inicialización del tablero
        tablero = [[True for j in range(n)] for i in range(n)]
        # llamada al método de anchura
        t1=time.clock()
        lista = caballo_anchura((x,y), tablero)
        t2=time.clock()
        tiempos.append(t2-t1)
        ejex.append(str((x,y)))

plt.figure()
plt.xlabel("Posiciones(x,y)")
plt.ylabel("Tiempo (segundos)")
plt.xticks(np.arange(9),(ejex))
plt.bar(np.arange(9),tiempos)
plt.show()
