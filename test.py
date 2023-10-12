import csv

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

print(buscar_cheques("C:/Full Stack ITBA/Sprint 4/Sprint4-Entrega/archivo.csv",12345678))