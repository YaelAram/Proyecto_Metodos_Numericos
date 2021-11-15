from math import sqrt
from tools.recta import Recta
import os


def obtener_error_pendiente(beta, n, s_x):
    return sqrt((n * (beta ** 2)) / ((n - 2) * (s_x ** 2) * (n - 1)))


def obtener_error_ordenada(beta, n, s_x, s_x2):
    return sqrt((s_x2 * (beta ** 2)) / ((n - 2) * ((n * s_x2) - (s_x ** 2))))


def obtener_beta(tam, datos, m, b):
    beta = 0.0
    for i in range(tam):
        beta += ((b + (m * datos[0][i]) - datos[1][i]) ** 2)
    return beta


def obtener_pendiente(n, s_x, s_y, s_xy, s_x2):
    return ((n * s_xy) - (s_x * s_y)) / ((n * s_x2) - (s_x ** 2))


def obtener_ordenada(n, s_x, s_y, s_xy, s_x2):
    return ((s_y * s_x2) - (s_x * s_xy)) / ((n * s_x2) - (s_x ** 2))


def obtener_r(n, s_x, s_y, s_xy, s_x2, s_y2):
    return ((n * s_xy) - (s_x * s_y)) / sqrt(((n * s_x2) - (s_x ** 2)) * ((n * s_y2) - (s_y ** 2)))


def obtener_coeficientes(tam, datos):
    x, y, x_2, y_2, xy = 0.0, 0.0, 0.0, 0.0, 0.0
    for i in range(tam):
        x += datos[0][i]
        y += datos[1][i]
        xy += (datos[0][i] * datos[1][i])
        x_2 += (datos[0][i] ** 2)
        y_2 += (datos[1][i] ** 2)
    return x, y, xy, x_2, y_2


def iniciar_consultas(iteraciones):
    print("\nIngresando consultas...\n")
    consultas = []
    for i in range(iteraciones):
        consultas.append(float(input(f"Consulta [{i}]: ")))
    return consultas


def iniciar_datos(iteraciones):
    print("\nIngresando datos...\n")
    datos = [[], []]
    for i in range(2):
        for j in range(iteraciones):
            datos[i].append(float(input(f"Dato [{i}][{j}]: ")))
    return datos


def iniciar_minimos():
    os.system("clear")
    print("Minimos Cuadrados\n")
    n = int(input("Numero de datos: "))
    datos = iniciar_datos(n)
    numero_consultas = int(input("\nNumero de consultas: "))
    consultas = iniciar_consultas(numero_consultas)
    s_x, s_y, s_xy, s_x2, s_y2 = obtener_coeficientes(n, datos)
    m, b = obtener_pendiente(n, s_x, s_y, s_xy, s_x2), obtener_ordenada(n, s_x, s_y, s_xy, s_x2)
    beta = obtener_beta(n, datos, m, b)
    error_pendiente = obtener_error_pendiente(beta, n, s_x)
    error_ordenada = obtener_error_ordenada(beta, n, s_x, s_x2)
    recta = Recta(m, b, None, None)
    print("\nResultados:\n")
    print(f"Coeficiente de correlacion lineal: {obtener_r(n, s_x, s_y, s_xy, s_x2, s_y2)}")
    print(f"Beta: {beta} \nError pendiente: {error_pendiente}")
    print(f"Error ordenada: {error_ordenada} \nEcuacion: {recta}")
    print("\nConsultas:\n")
    for consulta in consultas:
        print(f"y({consulta}) = {recta.evaluar(consulta)}")
