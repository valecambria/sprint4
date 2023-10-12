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

with open('C:/Full Stack ITBA/Sprint 4/Sprint4/archivo.csv', 'r') as archivocsv:
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

dni_ingresado = input('Ingrese su DNI:')
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
def buscarDNI(DNIbuscado):
    position = []
    encontrado = False
    i = 0
    while (i < len(DNI)):
        if (int(DNI[i]) == int(DNIbuscado)):
            position.append(i)
        i += 1
    return position



cant_dni = buscarDNI(dni_ingresado)
print("NroCheque | CodigoBanco | CodigoScurusal | NumeroCuentaOrigen | NumeroCuentaDestino | Valor | FechaOrigen | FechaPago | DNI | Estado")
for i in range (len(cant_dni)):
    print(f" {NroCheque[cant_dni[i]]} | {CodigoBanco[cant_dni[i]]} | {CodigoScurusal[cant_dni[i]]} | {NumeroCuentaOrigen[cant_dni[i]]} | {NumeroCuentaDestino[cant_dni[i]]} | {Valor[cant_dni[i]]} | {FechaOrigen[cant_dni[i]]} | {FechaPago[cant_dni[i]]} | {DNI[cant_dni[i]]} | {Estado[cant_dni[i]]}")


#print(buscarDNI(12345678)) #4


