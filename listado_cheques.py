import csv
import argparse
import datetime
import time

#----------------------------------- Entrada (inputs) por consola ------------------------------------------------

# Crear un objeto ArgumentParser
parser = argparse.ArgumentParser(description="Un ejemplo de cómo pasar parámetros por línea de comandos en Python")

# Argumentos obligatorios: Archivo.CSV, DNI, Pantalla y Tipo de Cheque
parser.add_argument("parametro_archivoCSV", type=str, help="Argumento obligatorio de tipo string con el nombre del archivo CSV.")

parser.add_argument("parametro_dni", type=str, help="Argumento obligatorio de tipo string con el numero de DNI del cliente.")

parser.add_argument("parametro_pantalla", type=str, help="Argumento obligatorio de tipo string con el tipo de salida [PANTALLA o CSV].")

parser.add_argument("parametro_tipo_cheque", type=str, help="Argumento obligatorio de tipo string con el tipo de cheque [EMITIDO o DEPOSITADO].")

# Argumentos opcionales: estado y fecha
parser.add_argument("--estado", type=str, help="Argumento opcional con el estado del cheque(PENDIENTE, APROBADO, RECHAZADO)")

parser.add_argument("--fecha", type=str, help="Argumento opcional con la fecha a partir de la cual mostrar los cheques.")

# Analizar los argumentos de la línea de comandos
args = parser.parse_args()

#-----------------------------------------Validacion de parámetros-------------------------------------------
validacion=True
if not args.parametro_dni.isnumeric():
    print("El DNI tiene que ser un numero")
    validacion=False
if not (args.parametro_tipo_cheque == 'EMITIDO' or args.parametro_tipo_cheque =='DEPOSITADO'):
    print("Debe especificar si el cheque fue emitido o depositado")
    validacion=False
if args.estado is not None and not (args.estado == 'PENDIENTE' or args.estado == 'APROBADO' or args.estado == 'RECHAZADO'):
    print("Debe especificar el estado del cheque correctamente (Aprobado, Pendiente o Rechazado)")
    validacion=False
def es_fecha_valida(fecha_str):
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')  # Ajusta el formato según tus necesidades
        return True
    except (ValueError, AttributeError): 
        return False
if not es_fecha_valida(args.fecha):
    print("Ingrese una fecha válida (YY-MM-DD)")
    validacion=False

#----------------------------------- Funcion filtrador  ------------------------------------------------

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

#Aplico el filtrado a los datos de entrada
filtrados = buscar_cheques(args.parametro_archivoCSV,args.parametro_dni,args.estado,args.fecha)

#------------------------------------------------------------------------------------

#----------------------------------- Salida (Outputs)  ------------------------------------------------

#Salida por pantalla

if (args.parametro_pantalla == 'PANTALLA' and validacion):
    #Mostrar por pantalla
    print("NroCheque | CodigoBanco | CodigoScurusal | NumeroCuentaOrigen | NumeroCuentaDestino | Valor | FechaOrigen | FechaPago | DNI | Estado")
    
    #Muestro todos los cheques con ese filtro
    for i in range (len(filtrados)):
        print(f" {filtrados[i]['NroCheque']} | {filtrados[i]['CodigoBanco']} | {filtrados[i]['CodigoScurusal']} | {filtrados[i]['NumeroCuentaOrigen']}| {filtrados[i]['NumeroCuentaDestino']} | {filtrados[i]['Valor']} | {filtrados[i]['FechaOrigen']} | {filtrados[i]['FechaPago']} | {filtrados[i]['DNI']} | {filtrados[i]['Estado']}")

#Salida por archivo
elif (args.parametro_pantalla == 'CSV' and validacion):
    # Fecha y hora actual
    ahora = datetime.datetime.now()
    cadena_fecha = ahora.strftime("%Y-%m-%d") #Pasa la fecha a formato año-mes-dia
    # Nombre archivo
    nombre_archivo = args.parametro_dni + "_" + cadena_fecha + '.csv'
    with open(nombre_archivo, 'w', newline='') as archivonuevo_csv:
        # Crear un escritor de CSV
        escritor_csv = csv.writer(archivonuevo_csv, quoting=csv.QUOTE_NONE, escapechar=' ') #Cambio el delimitador a espacio, sino se guarda con ""
        # Escribir los datos fila por fila
        texto =  'NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Estado'
        escritor_csv.writerow([texto])
        for i in range (len(filtrados)):
            datos = (f"{filtrados[i]['NroCheque']},{filtrados[i]['CodigoBanco']},{filtrados[i]['CodigoScurusal']},{filtrados[i]['NumeroCuentaOrigen']},{filtrados[i]['NumeroCuentaDestino']},{filtrados[i]['Valor']},{filtrados[i]['FechaOrigen']},{filtrados[i]['FechaPago']},{filtrados[i]['DNI']},{filtrados[i]['Estado']}")
            escritor_csv.writerow([datos])
elif validacion:
    print('Salida invalida. Solamente es posible por Pantalla o Archivo CSV')

#Codigos para testear

#python listado_cheques.py cheques.csv 12345678 PANTALLA EMITIDO
#python listado_cheques.py cheques.csv 98765432 CSV DEPOSITADO --fecha 2021-09-12:2
#python listado_cheques.py cheques.csv 55555555 PANTALLA EMITIDO --estado RECHAZADO