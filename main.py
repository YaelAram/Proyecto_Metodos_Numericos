import os
from model.gauss_seidel import iniciar_gauss_seidel
from model.jacobi import iniciar_jacobi
from model.interpolacion_lineal import iniciar_lineal
from model.interpolacion_lagrange import iniciar_lagrange
from model.minimos_cuadrados import iniciar_minimos
from model.mclaurin_ejecutar import iniciar_mclaurin


def main():
    while True:
        os.system('clear')
        print("Proyecto"
              "\n\nSeleccione una opcion:"
              "\n\n1. Metodo Gauss - Seidel"
              "\n2. Metodo Jacobi"
              "\n3. Interpolacion Lineal"
              "\n4. Interpolacion Polinomio de Lagrange"
              "\n5. Minimos Cuadrados"
              "\n6. Serie de McLaurin"
              "\n7. Salir\n")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            iniciar_gauss_seidel()
        elif opcion == 2:
            iniciar_jacobi()
        elif opcion == 3:
            iniciar_lineal()
        elif opcion == 4:
            iniciar_lagrange()
        elif opcion == 5:
            iniciar_minimos()
        elif opcion == 6:
            iniciar_mclaurin()
        else:
            print("\nSaliendo...")
            break
        if int(input("\n¿Deseas ingresar a otra seccion? (1/0): ")) != 1:
            break


if __name__ == '__main__':
    main()
