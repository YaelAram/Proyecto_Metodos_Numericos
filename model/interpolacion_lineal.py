from tools.recta import Recta
import os


def ingresar_datos(longitud):
    print(f"\nIngresando datos....\n")
    datos = [[], []]
    for i in range(longitud):
        datos[0].append(float(input(f"Dato [0][{i}]: ")))
    for i in range(longitud):
        datos[1].append(float(input(f"Dato [1][{i}]: ")))
    return datos


def ingresar_consultas(iteraciones):
    print(f"\nIngresando consultas....\n")
    consultas = []
    for i in range(iteraciones):
        consultas.append(float(input(f"Consulta [{i}]: ")))
    return consultas


def calcular(datos, valor):
    if (valor < datos[0][0]) or (valor > datos[0][-1]):
        return Recta(datos[0][0], datos[1][0], datos[0][-1], datos[1][-1])
    else:
        try:
            return datos[1][datos[0].index(valor)]
        except ValueError:
            for i in range(len(datos[0]) - 1):
                if datos[0][i] < valor < datos[0][i + 1]:
                    return Recta(datos[0][i], datos[1][i], datos[0][i + 1], datos[1][i + 1])


def iniciar_lineal():
    os.system("clear")
    print(f"Interpolacion y Extrapolacion Lineal\n")
    datos = ingresar_datos(int(input("Longitud de la tabla: ")))
    consultas = ingresar_consultas(int(input("\nNumero de consultas: ")))
    for consulta in consultas:
        resultado = calcular(datos, consulta)
        if type(resultado) is Recta:
            print(f"\nRecta: {resultado.__str__()} \nResultado: {resultado.evaluar(consulta)}")
        else:
            print(f"\nResultado: {resultado}")
