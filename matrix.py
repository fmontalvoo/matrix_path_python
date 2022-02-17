x = 0
arr = 0
pos = 0
opt = 0
rows = 0
cols = 0
total = 0
cantidad_de_pasos = 0

matrix = []
mtx_as_arr = []


def create_matrix():
    global matrix, mtx_as_arr
    for r in range(rows):
        matrix.append([0] * cols)
    mtx_as_arr = [0]*(rows*cols)


def array_to_matrix():
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = mtx_as_arr[r*cols+c]


def go_forward():
    sum = 0
    for i in range(total):
        mtx_as_arr[i] = 0
    
    for i in range(x):
        sum = pos[i] + cantidad_de_pasos
        if sum >= total:
            pos[i] = sum - total
        else:
            pos[i] = sum
        mtx_as_arr[pos[i]] = arr[i]
    array_to_matrix()


def go_backward():
    res = 0
    for i in range(total):
        mtx_as_arr[i] = 0
    
    for i in range(x):
        res = pos[i] - cantidad_de_pasos
        if res < 0:
            pos[i] = res + total
        else:
            pos[i] = res
        mtx_as_arr[pos[i]] = arr[i]
    array_to_matrix()


def display_matrix():
    print("\n")
    for row in matrix:
        print(row)


def enumerate_positions():
    global arr, pos
    arr = list(range(1, x+1))
    pos = list(range(0, x))


if __name__ == '__main__':
    rows = int(input("Ingrese la cantidad de filas: "))
    cols = int(input("Ingrese la cantidad de columnas: "))
    x = int(input("Cantidad de posiciones a enumerar: "))
    total = rows * cols
    create_matrix()
    enumerate_positions()
    go_forward()
    display_matrix()

    while(opt != 3):
        print("\nEscoga una direccion")
        print("1. Ir hacia adelante")
        print("2. Ir hacia atras")
        print("3. Salir del programa")
        opt = int(input("\nEscoga una opcion: "))

        if opt == 1:
            cantidad_de_pasos = int(input("Ingrese la cantidad de pasos a desplazar: "))
            if(cantidad_de_pasos <= total):
                go_forward()
                display_matrix()
            else:
                print("No puede desplazarse esa cantidad de pasos.\n")
        
        if opt == 2:
            cantidad_de_pasos = int(input("Ingrese la cantidad de pasos a desplazar: "))
            if(cantidad_de_pasos <= total):
                go_backward()
                display_matrix()
            else:
                print("No puede desplazarse esa cantidad de pasos.\n")
        
        if opt == 3:
            print("Saliendo del programa...")
            
