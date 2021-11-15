from tools.polinomio import Polinomio
import os


def constante(datos, tam):
    total = 0.0
    for i in range(tam):
        subtotal, semejante = datos[1][i], datos[0][i]
        for j in range(tam):
            if i != j:
                subtotal *= (-datos[0][j])
                subtotal *= ((semejante - datos[0][j]) ** -1)
        total += subtotal
    return total


def delta(sub):
    return (sub[0] * sub[1]) + (sub[2] * (sub[0] + sub[1]))


def lineal(datos, tam):
    total = 0.0
    for i in range(tam):
        subtotal, semejante, sub = datos[1][i], datos[0][i], []
        for j in range(tam):
            if i != j:
                sub.append(datos[0][j])
                subtotal *= ((semejante - datos[0][j]) ** -1)
        total += (subtotal * delta(sub))
    return total


def term_lineal_cuadrado(datos, tam):
    total = 0.0
    for i in range(tam):
        subtotal, semejante, b0_c0 = datos[1][i], datos[0][i], 0.0
        for j in range(tam):
            if i != j:
                b0_c0 += (-datos[0][j])
                subtotal *= ((semejante - datos[0][j]) ** -1)
        total += (subtotal * b0_c0)
    return total


def term_cuadrado_cubo(datos, tam):
    total, subtotales = 0.0, []
    for i in range(tam):
        subtotal, semejante = datos[1][i], datos[0][i]
        for j in range(tam):
            if i != j:
                subtotal *= ((semejante - datos[0][j]) ** -1)
        subtotales.append(subtotal)
        total += subtotal
    return total


def inicializar_consultas(iteraciones):
    print("\nIngresando consultas...\n")
    consultas = []
    for i in range(iteraciones):
        consultas.append(float(input(f"Consulta [{i}]: ")))
    return consultas


def inicializar_datos(iteraciones):
    print("\nIngresando datos...\n")
    datos = [[], []]
    for i in range(iteraciones):
        datos[0].append(float(input(f"Dato [0][{i}]: ")))
    for i in range(iteraciones):
        datos[1].append(float(input(f"Dato [1][{i}]: ")))
    return datos


def iniciar_lagrange():
    os.system("clear")
    print("Polinomio de Lagrange\n")
    numero_datos = int(input("Numero de registros: "))
    datos, fun = inicializar_datos(numero_datos), None
    numero_consultas = int(input("\nNumero de consultas: "))
    consultas = inicializar_consultas(numero_consultas)
    if numero_datos == 3:
        fun = Polinomio([term_cuadrado_cubo(datos, numero_datos), term_lineal_cuadrado(datos, numero_datos),
                         constante(datos, numero_datos)])
    elif numero_datos == 4:
        fun = Polinomio([term_cuadrado_cubo(datos, numero_datos), term_lineal_cuadrado(datos, numero_datos),
                         lineal(datos, numero_datos), constante(datos, numero_datos)])
    else:
        print("Numero de registros no soportado por el momento.")

    if fun is not None:
        print(f"\nEcuacion: {fun.__str__()}")
        for consulta in consultas:
            print(f"y({consulta}) = {fun.evaluar(consulta)}")
