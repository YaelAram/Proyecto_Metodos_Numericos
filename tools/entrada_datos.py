def ingresar_datos(iteraciones):
    print("\nIngresando datos...\n")
    datos = [[], []]
    for i in range(2):
        for j in range(iteraciones):
            datos[i].append(float(input(f"Dato [{i}][{j}]: ")))
    return datos


def ingresar_consultas():
    print(f"\nIngresando consultas....\n")
    consultas = []
    for consulta in input("Consultas: ").split():
        consultas.append(float(consulta))
    return consultas


