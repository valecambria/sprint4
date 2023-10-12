import csv

cant_variables = 10

# Creacion de variables para guardar los datos
NroCheque = []
CodigoBanco = []
CodigoScurusal = []
NumeroCuentaOrigen = []
NumeroCuentaDestino = []
Valor = []
FechaOrigen = []
FechaPago = []
DNI = []
Estado = []

#Guardo de datos en variables
with open('C:/Full Stack ITBA/Sprint 4/Sprint4-Entrega/archivo.csv', 'r') as archivocsv:
    lector = csv.reader(archivocsv)

    next(lector)

    for valor in lector:
        NroCheque.append(valor[0])
        CodigoBanco.append(valor[1])
        CodigoScurusal.append(valor[2])
        NumeroCuentaOrigen.append(valor[3])
        NumeroCuentaDestino.append(valor[4])
        Valor.append(valor[5])
        FechaOrigen.append(valor[6])
        FechaPago.append(valor[7])
        DNI.append(valor[8])
        Estado.append(valor[9])

#Inputs
dni_ingresado = int(input('Ingrese su DNI:'))
salida_ingresado = input('Que tipo de salida quiere: [PANTALLA - CSV]: ')
tipo_cheque_ingresado = input('Ingrese su tipo de cheque [EMITIDO - DEPOSITADO]')

si_estado_del_cheque = input('Quiere filtrar por estado del cheque?[S-N]: ')
if (si_estado_del_cheque == 'S'):
    estado_cheque_ingresado = input('(OPCIONAL) Estado del cheque [PENDIENTE-APROBADO-RECHAZADO]: ')

si_rango_de_fechas = input('Quiere filtrar por rango de fechas?[S-N]: ')
if (si_rango_de_fechas == 'S'):
    rango_fechas_desde_ingresado = input('(OPCIONAL) Rango desde: ')
    rango_fechas_hasta_ingresado = input('(OPCIONAL) Rango hasta: ')


#Buscar DNI
def buscar_cheques(archivo_csv, dni, estado=None, rango_desde=None, rango_hasta=None):
    resultados = []

    with open(archivo_csv, newline='') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            if int(fila["DNI"]) == int(dni):
                if estado is None or fila["Estado"] == estado:
                    if rango_desde is None or rango_hasta is None:
                        resultados.append(fila)
                    else:
                        fecha_pago = int(fila["FechaPago"])
                        if rango_desde <= fecha_pago <= rango_hasta:
                            resultados.append(fila)

    return resultados

#Filtro
filtrados = buscar_cheques("C:/Full Stack ITBA/Sprint 4/Sprint4-Entrega/archivo.csv",dni_ingresado)

##Mostrar por pantalla
if (salida_ingresado == 'PANTALLA'):
    print("NroCheque | CodigoBanco | CodigoScurusal | NumeroCuentaOrigen | NumeroCuentaDestino | Valor | FechaOrigen | FechaPago | DNI | Estado")
    #Muestro todos los cheques con ese filtro
    for i in range (len(filtrados)):
        print(f" {filtrados[i]['NroCheque']} | {filtrados[i]['CodigoBanco']} | {filtrados[i]['CodigoScurusal']} | {filtrados[i]['NumeroCuentaOrigen']}| {filtrados[i]['NumeroCuentaDestino']} | {filtrados[i]['Valor']} | {filtrados[i]['FechaOrigen']} | {filtrados[i]['FechaPago']} | {filtrados[i]['DNI']} | {filtrados[i]['Estado']}")
elif (salida_ingresado == 'CSV'):
    """with open('datos.csv', 'w', newline='') as archivonuevo_csv:
        # Crear un escritor de CSV
        escritor_csv = csv.writer(archivonuevo_csv)
        # Escribir los datos fila por fila
        escritor_csv.writerow("NroCheque,CodigoBanco,CodigoScurusal,NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Estado")
        for i in range (len(cant_dni)):
            datos = (f" {NroCheque[cant_dni[i]]},{CodigoBanco[cant_dni[i]]},{CodigoScurusal[cant_dni[i]]},{NumeroCuentaOrigen[cant_dni[i]]},{NumeroCuentaDestino[cant_dni[i]]},{Valor[cant_dni[i]]},{FechaOrigen[cant_dni[i]]},{FechaPago[cant_dni[i]]},{DNI[cant_dni[i]]},{Estado[cant_dni[i]]}")
            escritor_csv.writerow(datos)"""

#print(buscarDNI(12345678)) #4


