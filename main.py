import os
from model.interpolacion_lineal import iniciar_lineal
from model.interpolacion_cuadratica import iniciar_cuadratica
from model.interpolacion_lagrange import iniciar_lagrange
from model.minimos_cuadrados import iniciar_minimos
from tools.ayuda import ayuda


def main():
    while True:
        os.system("cls")
        print("Proyecto Metodos Numericos 3.0\n"
              "Castillo Sanchez Yael Aram - Hernandez Soledad Angel Agustin - Garcia Cordova Montse\n\n"
              "https://github.com/YaelAram/Proyecto_Metodos_Numericos\n\n"
              "Escribe 'ayuda' para obtener ayuda.\n\n"
              "Seleccione una opcion:\n\n"
              "1. Interpolacion Lineal\n"
              "2. Interpolacion Cuadratica\n"
              "3. Interpolacion Polinomio de Lagrange\n"
              "4. Minimos Cuadrados\n"
              "5. Salir\n")
        opcion = input("Opcion: ")
        if opcion == "1":
            iniciar_lineal()
        elif opcion == "2":
            iniciar_cuadratica()
        elif opcion == "3":
            iniciar_lagrange()
        elif opcion == "4":
            iniciar_minimos()
        elif opcion == "5":
            print("\nSaliendo...")
            break
        else:
            if opcion.lower() == "ayuda":
                ayuda()
            else:
                print(f"\nComando {opcion} no reconocido.")
        if int(input("\n¿Deseas ingresar a otra seccion? (1/0): ")) != 1:
            break


if __name__ == '__main__':
    main()
