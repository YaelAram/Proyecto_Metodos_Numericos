import os
from model.interpolacion_lineal import iniciar_lineal
from model.interpolacion_cuadratica import iniciar_cuadratica
from model.interpolacion_lagrange import iniciar_lagrange
from model.minimos_cuadrados import iniciar_minimos


def main():
    while True:
        os.system('clear')
        print("Proyecto"
              "\n\nSeleccione una opcion:"
              "\n1. Interpolacion Lineal"
              "\n2. Interpolacion Cuadratica"
              "\n3. Interpolacion Polinomio de Lagrange"
              "\n4. Minimos Cuadrados"
              "\n5. Salir\n")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            iniciar_lineal()
        elif opcion == 2:
            iniciar_cuadratica()
        elif opcion == 3:
            iniciar_lagrange()
        elif opcion == 4:
            iniciar_minimos()
        else:
            print("\nSaliendo...")
            break
        if int(input("\n¿Deseas ingresar a otra seccion? (1/0): ")) != 1:
            break


if __name__ == '__main__':
    main()
