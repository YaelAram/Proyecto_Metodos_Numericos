from math import sqrt
from tools.recta import Recta
from tools.entrada_datos import ingresar_datos, ingresar_consultas
import os


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


def iniciar_minimos():
    os.system("clear")
    print("Minimos Cuadrados\n")
    n = int(input("Numero de datos: "))
    datos = ingresar_datos(n)
    consultas = ingresar_consultas()
    s_x, s_y, s_xy, s_x2, s_y2 = obtener_coeficientes(n, datos)
    m, b = obtener_pendiente(n, s_x, s_y, s_xy, s_x2), obtener_ordenada(n, s_x, s_y, s_xy, s_x2)
    beta = obtener_beta(n, datos, m, b)
    recta = Recta(m, b, None, None)
    print("\nResultados:\n")
    print(f"Coeficiente de correlacion lineal: {obtener_r(n, s_x, s_y, s_xy, s_x2, s_y2)}")
    print(f"Beta: {beta} \nEcuacion: {recta}")
    print("\nConsultas:\n")
    for consulta in consultas:
        print(f"y({consulta}) = {recta.evaluar(consulta)}")
