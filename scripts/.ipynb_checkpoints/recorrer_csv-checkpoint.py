import csv

nombre_archivo = 'archivo_csv.csv'

def archivo_csv():

    with open(nombre_archivo) as f:

         lector_csv = csv.reader(f)

         encabezado = next(lector_csv)
         #print(encabezado)

         for registro in lector_csv:
              print(registro[0])

archivo_csv()

                    

