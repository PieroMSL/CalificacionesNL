from CalificacionesNL_V1_1 import Calificador


if __name__ == '__main__':
    # Obtener la nota del usuario
    nota_usuario = float(input("Nota: "))

    # Crear una instancia de la clase Calificador
    calificador = Calificador(nota_usuario)

    # Calificar la nota y mostrar el resultado
    categoria = calificador.calificar()
    print("La Nota es", categoria + ".")



