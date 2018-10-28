import time

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
while True:
    x=int(input('Coordenada x de casilla inicial (entre 0 y {}): '.format(n-1)))
    y=int(input('Casilla inicial (segunda coordenada, entre 0 y {}): '.format(n-1)))
    if x in range(n) and y in range(n):
        break

# Método de búsqueda en profundidad -------------------------------------------------
print("\nBusqueda en profundidad")

# inicialización del tablero
tablero = [[True for j in range(n)] for i in range(n)]

# llamada al método de backtracking
t1=time.clock()
nodos=0
lista = caballo_profundidad((x,y), tablero,[])
t2=time.clock()

# tiempo de resolución
print("Tiempo empleado en obtener todas las solución: ",t2-t1)

#nodos atravesados
print("Nodos atravesados: ", nodos)

#separar las soluciones en listas de 25 elementos
soluciones=[]
for i in range(1,len(lista)+1):
	if i%(n*n)==0:
		soluciones.append(lista[int(i-n*n):int(i)])
