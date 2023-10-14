import argparse

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(description="Un ejemplo de cómo pasar parámetros por línea de comandos en Python")

# Agregar un argumento obligatorio
parser.add_argument("parametro_dni", type=int, help="Este es un argumento obligatorio de tipo entero.")

# Agregar un argumento obligatorio
parser.add_argument("parametro_pantalla", type=str, help="Este es un argumento obligatorio de tipo entero 2.")

# Agregar un argumento opcional
parser.add_argument("--parametro_opcional", type=str, help="Este es un argumento opcional de tipo cadena.")

# Analizar los argumentos de la línea de comandos
args = parser.parse_args()

# Acceder a los argumentos
print("Argumento Obligatorio:", args.parametro_dni)
# Acceder a los argumentos
print("Argumento Obligatorio:", args.parametro_pantalla)

if args.parametro_opcional:
    print("Argumento Opcional:", args.parametro_opcional)
