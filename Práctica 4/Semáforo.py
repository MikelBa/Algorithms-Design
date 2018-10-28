import random


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



def imprimir_soluciones(sol):
    C=["AB","AC","AD","BA","BC","BD","DA","DB","DC","EA","EB","EC","ED"]
    for i in range(len(sol)):
        for j in range(len(sol[i])):
            sol[i][j]=C[sol[i][j]]
    return sol



       
C=[0,1,2,3,4,5,6,7,8,9,10,11,12]        
matriz=[[0,0,0,0,1,1,1,1,0,1,1,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,1,0,0,0,1,1,1,1],[0,0,0,0,0,0,1,0,0,1,0,0,0],[1,1,0,0,0,0,0,1,1,0,1,1,0],[1,1,1,0,0,0,1,0,0,0,1,1,1],[1,1,0,1,0,1,0,0,0,1,1,1,0],[1,1,0,0,1,0,0,0,0,0,1,1,0],[0,1,0,0,1,0,0,0,0,0,0,1,0],[1,1,1,1,0,0,1,0,0,0,0,0,0],[1,1,1,0,1,1,1,1,0,0,0,0,0],[0,1,1,0,1,1,1,1,1,0,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,0]]
smax2=semaforos_max(matriz, C)
print("Solución con semaforos_max:\n",imprimir_soluciones(smax2),"\n")


C=[0,1,2,3,4,5,6,7,8,9,10,11,12]        
matriz=[[0,0,0,0,1,1,1,1,0,1,1,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,1,0,0,0,1,1,1,1],[0,0,0,0,0,0,1,0,0,1,0,0,0],[1,1,0,0,0,0,0,1,1,0,1,1,0],[1,1,1,0,0,0,1,0,0,0,1,1,1],[1,1,0,1,0,1,0,0,0,1,1,1,0],[1,1,0,0,1,0,0,0,0,0,1,1,0],[0,1,0,0,1,0,0,0,0,0,0,1,0],[1,1,1,1,0,0,1,0,0,0,0,0,0],[1,1,1,0,1,1,1,1,0,0,0,0,0],[0,1,1,0,1,1,1,1,1,0,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,0]]
smin2=semaforos_min(matriz, C)
print("Solución con semaforos_min:\n",imprimir_soluciones(smin2),"\n")


C=[0,1,2,3,4,5,6,7,8,9,10,11,12]        
matriz=[[0,0,0,0,1,1,1,1,0,1,1,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,1,0,0,0,1,1,1,1],[0,0,0,0,0,0,1,0,0,1,0,0,0],[1,1,0,0,0,0,0,1,1,0,1,1,0],[1,1,1,0,0,0,1,0,0,0,1,1,1],[1,1,0,1,0,1,0,0,0,1,1,1,0],[1,1,0,0,1,0,0,0,0,0,1,1,0],[0,1,0,0,1,0,0,0,0,0,0,1,0],[1,1,1,1,0,0,1,0,0,0,0,0,0],[1,1,1,0,1,1,1,1,0,0,0,0,0],[0,1,1,0,1,1,1,1,1,0,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,0]]
saz2=semaforos_azar(matriz, C)
print("Solución con semaforos_azar:\n",imprimir_soluciones(saz2),"\n")

C=[0,1,2,3,4,5,6,7,8,9,10,11,12]        
matriz=[[0,0,0,0,1,1,1,1,0,1,1,0,0],[0,0,0,0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,1,0,0,0,1,1,1,1],[0,0,0,0,0,0,1,0,0,1,0,0,0],[1,1,0,0,0,0,0,1,1,0,1,1,0],[1,1,1,0,0,0,1,0,0,0,1,1,1],[1,1,0,1,0,1,0,0,0,1,1,1,0],[1,1,0,0,1,0,0,0,0,0,1,1,0],[0,1,0,0,1,0,0,0,0,0,0,1,0],[1,1,1,1,0,0,1,0,0,0,0,0,0],[1,1,1,0,1,1,1,1,0,0,0,0,0],[0,1,1,0,1,1,1,1,1,0,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,0]]
saz2=semaforos_azar(matriz, C)
print("Solución con semaforos_azar:\n",imprimir_soluciones(saz2),"\n")
