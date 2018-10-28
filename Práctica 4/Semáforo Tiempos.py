import random
import numpy as np
import time
import matplotlib.pyplot as plt

def sym_mat(n):
    a = np.random.random_integers(0,1,size=(n,n))
    matrix = np.tril(a) + np.tril(a, -1).T
    matrix=np.ndarray.tolist(matrix)
    return matrix


def semaforos_max (matriz, C):
    n_nodos=len(C)
    nodo_inicial=elegir_nodo_max(matriz, C)
    colores=[[nodo_inicial]]
    C.remove(nodo_inicial)
    while len(C)!=0:
        n0=elegir_nodo_max(matriz, C)
        C.remove(n0)
        insertado=False
        for i in range(len(colores)):
            if insertado==False:
                cont=0
                for nodo in colores[i]:
                    if matriz[n0][nodo]==1:
                        cont=cont+1
                if cont==0:
                    colores[i].append(n0)
                    insertado=True
        if insertado==False:
            colores.append([n0])
    return colores
                

def elegir_nodo_max (matriz, C):
    #elegiremos el nodo con más conexiones
    maxim=0
    nodo_max=0
    for i in range(len(matriz)):
        if i in C:
            cont=0
            for j in range(len(matriz)):
                if matriz[i][j]==1:
                    cont=cont+1
            if cont>maxim:
                maxim=cont
                nodo_max=i
    return nodo_max




def semaforos_min (matriz, C):
    n_nodos=len(C)
    nodo_inicial=elegir_nodo_min(matriz, C)
    colores=[[nodo_inicial]]
    C.remove(nodo_inicial)
    while len(C)!=0:
        n0=elegir_nodo_min(matriz, C)
        C.remove(n0)
        insertado=False
        for i in range(len(colores)):
            if insertado==False:
                cont=0
                for nodo in colores[i]:
                    if matriz[n0][nodo]==1:
                        cont=cont+1
                if cont==0:
                    colores[i].append(n0)
                    insertado=True
        if insertado==False:
            colores.append([n0])
    return colores

def elegir_nodo_min (matriz, C):
    #elegiremos el nodo con menos conexiones
    minimo=len(matriz)
    nodo=0
    for i in range(len(matriz)):
        if i in C:
            cont=0
            for j in range(len(matriz)):
                if matriz[i][j]==1:
                    cont=cont+1
            if cont<minimo:
                minimo=cont
                nodo=i
    return nodo




def semaforos_azar (matriz, C):
    n_nodos=len(C)
    nodo_inicial=random.randrange(len(C))
    colores=[[nodo_inicial]]
    C.remove(nodo_inicial)
    while len(C)!=0:
        n0=random.choice(C)
        C.remove(n0)
        insertado=False
        for i in range(len(colores)):
            if insertado==False:
                cont=0
                for nodo in colores[i]:
                    if matriz[n0][nodo]==1:
                        cont=cont+1
                if cont==0:
                    colores[i].append(n0)
                    insertado=True
        if insertado==False:
            colores.append([n0])
    return colores



#### PROGRAMA PRINCIPAL ####

print("\nGráficos de tiempo dependiendo del valor de n: ")
tiempos=[]
ejex=[]
tiempo=[]
for n in range(12,100):
    ejex.append(n)
    tiempo1=0
    for i in range(1000):
        # inicialización de C y dematriz
        C=list(range(n))
        matriz=sym_mat(n)
        # llamada al método
        start_time = time.time()
        #semaforos_min(matriz, C)
        #semaforos_max(matriz, C)
        semaforos_azar(matriz, C)
        elapsed_time = time.time() - start_time
        tiempo1=elapsed_time+tiempo1
    tiempo.append(tiempo1)



plt.plot(ejex,tiempo)
plt.xlabel("n (número entero)")
plt.ylabel("Tiempo (segundos)")
#plt.title("Tiempo de ejecución de semaforos_min con lista C de tamaño n") 
#plt.title("Tiempo de ejecución de semaforos_max con lista C de tamaño n")
plt.title("Tiempo de ejecución de semaforos_azar con lista C de tamaño n") 
plt.show()


