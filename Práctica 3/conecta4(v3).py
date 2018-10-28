###Función para imprimir el tablero en la pantalla:
def imprimir_tablero(nodo):
    print("\n")
    for i in range(5,-1,-1):
        print("\t", end="")
        for j in range(7):
            print("| " + str(nodo[i][j]), end=" ")
        print("|")
    print("\t  _   _   _   _   _   _   _")
    print("\t  1   2   3   4   5   6   7 \n")

###############################EVALUACIÓN###############################
###A las siguientes funciones les damos el nodo actual y la posición de partida (i,j)
##y devuelven 1 si desde esa posición hay un numero n (n=linea) seguido de fichas del mismo color, sino devuelve 0.

def derecha(nodo,fil,col,linea):
    final=col+linea-1
    if final>=7:
        return 0
    else:
        conectados=1
        for j in range (col+1,final+1):
            if nodo[fil][j]==nodo[fil][col]:
                conectados+=1
            else:
                break
        if conectados>=linea:
            if linea!=4:
                if col-1>=0:
                    if nodo[fil][col-1]=="-":
                        return 1
                if col+linea<=6:
                    if nodo[fil][col+linea]=="-":
                        return 1
                return 0
            else:
                return 1
        else:
            return 0

def arriba(nodo,fil,col,linea):
    final=fil+linea-1
    if final>=6:
        return 0
    else:
        conectados=1
        for i in range (fil+1,final+1):
            if nodo[i][col]==nodo[fil][col]:
                conectados+=1
            else:
                break
        if conectados>=linea:
            if linea!=4:
                if fil-1>=0:
                    if nodo[fil-1][col]=="-":
                        return 1
                if fil+linea<=5:
                    if nodo[fil+linea][col]=="-":
                        return 1
                return 0
            else:
                return 1
        else:
            return 0

def diag_der(nodo,fil,col,linea):
    final_fil=fil+linea-1
    final_col=col+linea-1
    if final_fil>=6 or final_col>=7:
        return 0
    else:
        conectados=1
        for i in range (1,linea):
            if nodo[fil+i][col+i]==nodo[fil][col]:
                conectados+=1
            else:
                break
        if conectados>=linea:
            if linea!=4:
                if fil-1>=0 and col-1>=0:
                    if nodo[fil-1][col-1]=="-":
                        return 1
                if fil+linea<=5 and col+linea<=6:
                    if nodo[fil+linea][col+linea]=="-":
                        return 1
                return 0
            else:
                return 1
        else:
            return 0

def diag_izq(nodo,fil,col,linea):
    final_fil=fil+linea-1
    final_col=col-linea+1
    if final_fil>=6 or final_col<0:
        return 0
    else:
        conectados=1
        for i in range (1,linea):
            if nodo[fil+i][col-i]==nodo[fil][col]:
                conectados+=1
            else:
                break
        if conectados>=linea:
            if linea!=4:
                if fil-1>=0 and col+1<=6:
                    if nodo[fil-1][col+1]=="-":
                        return 1
                if fil+linea<=5 and col-linea>=0:
                    if nodo[fil+linea][col-linea]=="-":
                        return 1
                return 0
            else:
                return 1
        else:
            return 0

def evaluar(nodo):
    ##Herística para evaluar el nodo:
    ##99999*(nº de 4 en raya pc)+100*(nº de 3 en raya pc)+10*(nº de 2 en raya pc)
    ##-99999*(nº de 4 en raya rival)-100*(nº de 3 en raya rival)-10*(nº de 2 en raya rival)
    cont2_o=0
    cont2_x=0
    cont3_o=0
    cont3_x=0
    cont4_o=0
    cont4_x=0
    for i in range(6):
        for j in range(7):
            if nodo[i][j]=="o":
                cont2_o+=derecha(nodo,i,j,2)+arriba(nodo,i,j,2)+diag_der(nodo,i,j,2)+diag_izq(nodo,i,j,2)
                cont3_o+=derecha(nodo,i,j,3)+arriba(nodo,i,j,3)+diag_der(nodo,i,j,3)+diag_izq(nodo,i,j,3)
                cont4_o+=derecha(nodo,i,j,4)+arriba(nodo,i,j,4)+diag_der(nodo,i,j,4)+diag_izq(nodo,i,j,4)

            elif nodo[i][j]=="x":
                cont2_x+=derecha(nodo,i,j,2)+arriba(nodo,i,j,2)+diag_der(nodo,i,j,2)+diag_izq(nodo,i,j,2)
                cont3_x+=derecha(nodo,i,j,3)+arriba(nodo,i,j,3)+diag_der(nodo,i,j,3)+diag_izq(nodo,i,j,3)
                cont4_x+=derecha(nodo,i,j,4)+arriba(nodo,i,j,4)+diag_der(nodo,i,j,4)+diag_izq(nodo,i,j,4)

    if cont4_o>0:
        return -999999
    elif cont4_x>0:
        return 999999
    else:
        return 100*cont3_x+cont2_x-100*cont3_o-cont2_o

def juegoterminado(nodo):
###Esta función nos devuelve True si el juego ha acabado y Fasle si no.
###En caso de que el juego haya acabado tambien devuelve quien es el ganador y la posición.
    for i in range(6):
        for j in range(7):
            if nodo[i][j]!='-':
                if derecha(nodo,i,j,4)==1 or arriba(nodo,i,j,4)==1 or diag_der(nodo,i,j,4)==1 or diag_izq(nodo,i,j,4)==1:
                    return [True,nodo[i][j],i,j]
    return False

def imprimir_ganador(nodo,fil,col,W):
    if derecha(nodo,fil,col,4)==1:
        for i in range(4):
            nodo[fil][col+i]=W
    elif arriba(nodo,fil,col,4)==1:
        for i in range(4):
            nodo[fil+i][col]=W
    elif diag_der(nodo,fil,col,4)==1:
        for i in range(4):
            nodo[fil+i][col+i]=W
    else:
        for i in range(4):
            nodo[fil+i][col-i]=W
    return nodo


def sucesores(nodo,turno):
###Nos devuelve los sucesores de un nodo y para cada sucesor
###la columna donde se ha metido la nueva ficha.
    suces=[]
    for j in range(7):
        numfich=nodo[6][j]
        if numfich<6:
            if turno=="turnomax":
                fila=nodo[numfich][:]
                cantidades=nodo[6][:]
                fila[j]="x"
                cantidades[j]+=1
                nodo[numfich]=fila[:]
                nodo[6]=cantidades[:]
                suces.append([nodo[:][:],j])
                fila[j]="-"
                cantidades[j]-=1
                nodo[numfich]=fila[:]
                nodo[6]=cantidades[:]
            else:
                fila=nodo[numfich][:]
                cantidades=nodo[6][:]
                fila[j]="o"
                cantidades[j]+=1
                nodo[numfich]=fila[:]
                nodo[6]=cantidades[:]
                suces.append([nodo[:][:],j])
                fila[j]="-"
                cantidades[j]-=1
                nodo[numfich]=fila[:]
                nodo[6]=cantidades[:]
    return suces


def minimax(nodo,n,turno):
    alpha=-999999
    beta=999999
    move=""
    columna=""
    S=sucesores(nodo,turno)
    if n==0 or len(S)==0 or juegoterminado(nodo)!=False:
        Minimax=evaluar(nodo)
        move=nodo
        columna=0
    else:
        parar=False
        if turno=="turnomax":
            while parar==False:
                w=S[0][0]
                v=S[0][1]
                del S[0]
                res_minimax=minimax(w,n-1,"turnomin")
                if alpha<=res_minimax[0]:
                    alpha=res_minimax[0]
                    move=w
                    columna=v
                if beta<=alpha or len(S)==0:
                    parar=True
            Minimax=alpha
        else:
            while parar==False:
                w=S[0][0]
                v=S[0][1]
                del S[0]
                res_minimax=minimax(w,n-1,"turnomax")
                if beta>=res_minimax[0]:
                    beta=res_minimax[0]
                    move=w
                    columna=v
                if beta<=alpha or len(S)==0:
                    parar=True
            Minimax=beta
    return [Minimax,move,columna]

def movimiento(nodo,col,o):
    col=col-1
    fil=nodo[6][col]
    nodo[6][col]+=1
    nodo[fil][col]=o
    return nodo

#########################################################JUEGO JUEGO JUEGO JUEGO JUEGO######################################################### 
jugar=str(input("Bienvenido. ¿Quieres jugar al conecta 4? (si o no) "))

while jugar!="si" and jugar!="no":
    jugar=str(input("Por favor, responde a la pregunta con un si o no. ¿Quieres jugar al conecta 4? "))

while jugar=="si":

    ## Creamos el tablero. Las listas dentro de la lista son filas y los elementos de esas listas columnas.     
    tablero=[["-" for j in range(7)] for i in range(6)]
    ## Añadimos un ultimo vector a la lista con la cantidad de fichas de cada columna:
    tablero.append([0,0,0,0,0,0,0])

    dif=int(input("Elige el nivel de dificultad (1-4): "))
    while dif<0 or dif>5:
        dif=int(input("El nivel de dificultad tiene que estar entre 1-8. Vuelve a elegirlo: "))
        
    empezar=str(input("¿Quieres empezar tu el juego? (si o no) "))
    while empezar!="si" and empezar!="no":
        empezar=str(input("Por favor, responde a la pregunta con un si o no. ¿Quieres empezar tu el juego? "))
    if empezar=="si":
        turno=1
    else:
        turno=0

    imprimir_tablero(tablero)

    while juegoterminado(tablero)==False and sum(tablero[6])!=42:
        if turno%2==0:
            hacer_minimax=minimax(tablero,dif,"turnomax")
            print("Es el turno del ordenador. Ha introducido una ficha en la columna "+str(hacer_minimax[2]+1)+".")
            tablero=hacer_minimax[1]
            imprimir_tablero(tablero)
            turno+=1
        else:
            c=int(input("Es tu turno. Elige una columna: "))
            while c<1 or c>8:
                c=int(input("Has introducido un valor incorrecto. Elige una columna: "))
            
            while tablero[6][c-1]==6:
                c=int(input("La columna que has elegido esta llena. Elige otra: "))
            tablero=movimiento(tablero,c,"o")
            imprimir_tablero(tablero)
            turno+=1

    if sum(tablero[6])==42:
        print("Empate.")
    else:
        ganador=juegoterminado(tablero)
        if ganador[1]=="o":
            print("¡Enhorabuena, has ganado!")
            imprimir_tablero(imprimir_ganador(tablero,ganador[2],ganador[3],"O"))
        else:
            print("Has perdido.")
            imprimir_tablero(imprimir_ganador(tablero,ganador[2],ganador[3],"X"))
    jugar=str(input("¿Quieres volver a jugar al conecta 4? (si o no) "))

    while jugar!="si" and jugar!="no":
        jugar=str(input("Por favor, responde a la pregunta con un si o no. ¿Quieres jugar al conecta 4? "))

print("¡Hasta la próxima!")



