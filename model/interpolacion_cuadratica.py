from tools.polinomio import Polinomio
from model.gauss_jordan import calcular_gauss_jordan
from tools.entrada_datos import ingresar_consultas
import os


def ingresar_datos():
    print(f"\nIngresando datos....\n")
    datos = [[], [], []]
    for i in range(2):
        for j in range(3):
            dato = float(input(f"Dato [{i}][{j}]: "))
            if i == 0:
                datos[j].append(float(dato ** 2))
                datos[j].append(float(dato))
                datos[j].append(1.0)
            else:
                datos[j].append(float(dato))
    return datos


def iniciar_cuadratica():
    os.system("clear")
    print(f"Interpolacion y Extrapolacion Cuadratica\n")
    fun = Polinomio(calcular_gauss_jordan(ingresar_datos(), 3, 4))
    consultas = ingresar_consultas()
    print(f"Funcion = y(x) = {fun.__str__()}")
    for consulta in consultas:
        print(f"y({consulta}) = {fun.evaluar(consulta)}")
