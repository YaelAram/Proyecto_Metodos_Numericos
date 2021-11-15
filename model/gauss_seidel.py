from decimal import *
import os
getcontext().prec = 64


def error(valor_actual, valor_anterior):
    return abs((valor_actual - valor_anterior) / valor_actual)


def crear_matriz_resultados(fil):
    resultados = []
    for i in range(fil):
        resultados.append(Decimal("0.0"))
    return resultados


def calcular(mat, fil):
    resultados, errores = crear_matriz_resultados(fil), crear_matriz_resultados(fil)
    for i in range(100_000):
        for index, exp in enumerate(mat):
            resultado_aux = exp[-1]
            for pos, term in enumerate(exp):
                if pos != index and pos < (len(exp) - 1):
                    resultado_aux += -(term * resultados[pos])
            resultado_aux *= Decimal(1 / exp[index])
            errores[index] = error(resultado_aux, resultados[index])
            resultados[index] = resultado_aux
    return resultados, errores


def crear_matriz(num_fil, num_col):
    print("\nIngresando datos de la matriz...\n")
    matriz = []
    for i in range(num_fil):
        lista_aux = []
        for j in range(num_col):
            lista_aux.append(Decimal(input(f"Ingresa el dato[{i}][{j}]: ")))
        matriz.append(lista_aux)
    return matriz


def iniciar_gauss_seidel():
    os.system("clear")
    print("Metodo Guss - Seidel\n\n")
    tam_fila, tam_columna = int(input("Numero de filas: ")), int(input("Numero de columnas: "))
    if tam_fila == (tam_columna - 1) and 0 < tam_fila <= 10:
        matriz = crear_matriz(tam_fila, tam_columna)
        resultados, errores = calcular(matriz, tam_fila)
        incognita = 112
        for i in range(tam_fila):
            print(f"\nIncognita - {chr(incognita)}: {resultados[i]} \nError (%): {errores[i] * 100}")
            incognita += 1
    else:
        print("La matriz de coeficientes no es cuadrada, intenta de nuevo.")
