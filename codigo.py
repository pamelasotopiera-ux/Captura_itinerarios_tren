import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import funciones_fecha as ff






def itinerario(fecha,origen,destino,servicio=1):
    url=f"https://www.efe.cl/planificador/?empresa={servicio}&hsalida=0&hregreso&usuario=1&ida=1&origen={origen}&destino={destino}&salida={fecha}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text ,'html.parser')
    
    tabla = soup.find('table', class_='table tablaTren f-size-14 f-face-roboto bg-color-gris-2')

    datos = []
    hora_actual= datetime.now()
    if tabla:  
        for fila in tabla.find_all('tr')[1:]: 
            celdas = fila.find_all('td')
            if len(celdas) >= 4:  
                datos.append({
                    'salida': ff.incrementar_date(fecha,celdas[0].text.strip()),
                    'llegada': ff.incrementar_date(fecha,celdas[1].text.strip()),
                    'duracion': celdas[2].text.strip(),
                    'precio': celdas[3].text.strip()
                })

        contador=0
        for salida in datos:  
            if salida['salida'] > hora_actual:
                contador=contador+1
                print(salida['salida'])
        if contador==0:
            print ('No hay más salidas el día de hoy')
     
    

 


    

    
    
    
    #salidas=celdas[0].text.strip()

    #print(f'en la fecha {fecha} hay {len(datos)} salidas')
    #print(datos)

    #return salidas
  
itinerario('2026-06-16','13','1')


"""1.-mostrar las salidas posteriores a la hora actual
   calcular hora actual
   las salidas
   def mostrar_proximas_salidas(las salidas, hora actual)
   convertir string a datetime
   comparar las salidas con hora actual
   si las salidas es mayor que hora actual
   mostrar las salidas
   Si no colocar mensaje de No hay salidas posteriores
    
2.-hacer que los parametros sean opcionales
   investigar cómo se realizan los parámetros opcionales (por defecto)
3.-mensaje de error para consulta no realizada
   Listar errores posibles
   Ubicarlos en el código
4.-testear las funciones
    Testeo unitario
     elaborar los casos de prueba
     realizar las pruebas
5.-guardar el itinerario en un archivo
   consultar itinerario
   Guardarlo como JSON.
6.- Documentación."""

