import csv, argparse

"""
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
    print("Argumento Opcional:", args.parametro_opcional)"""


#Filtrador (corte de control segun los filtros indicados)
def buscar_cheques(archivo_csv, dni, estado, rango):
    resultados = [] #Se guardan los resultados en una lista

    with open(archivo_csv, newline='') as archivo: #Apertura del archivo
        lector_csv = csv.DictReader(archivo) #Asigno el archivo a una variable
        for fila in lector_csv:
            #CORTE DE CONTROL: Primero por el DNI
            if str(fila["DNI"]) == str(dni):
                #Luego por el estado del cheque
                if estado is None or fila["Estado"].upper() == estado.upper():
                    #Por ultimo, el rango de fechas
                    if rango is None:
                        resultados.append(fila)
                    else:
                        fecha_pago = fila["FechaPago"]
                        #Si esta entre ese rango lo guardo, las fechas estan en timestap
                        if rango >= fecha_pago:
                            resultados.append(fila)

    return resultados


filtrados = buscar_cheques("C:/Full Stack ITBA/Sprint 4/Sprint4-Entrega/cheques.csv","12345678","","")

#Funcion que comprueba si hay cheques repetidos para el mismo cliente
def cheques_repetidos(lista):
    repite = False
    for fila1 in lista:
        repetidos = 0
        for fila2 in lista:
            if fila1["DNI"] == fila2["DNI"]:
                repetidos += 1
            if repetidos > 1: #Si existen mas de 2 cheques, entonces hay repetidos
                repite = True
    return repite

print(cheques_repetidos(filtrados))