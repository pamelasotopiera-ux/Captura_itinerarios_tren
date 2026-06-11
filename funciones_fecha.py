from datetime import datetime
from datetime import datetime, date, time,timedelta


# Opción 1: hacer el datetime desde la concatenación los string fecha y hora
fecha='2026-06-05'
salida='08:20'
def unir_fecha_hora(fecha, hora):
    fecha_hora=fecha+" "+hora
    formato='%Y-%m-%d %H:%M'
    return(datetime.strptime(fecha_hora,formato))

# Opción 2: componer desde fecha como date y hora como time
def componer_date_time(fecha, hora):
    formato_fecha='%Y-%m-%d'
    formato_hora='%H:%M'
    parte_hora=datetime.strptime(hora,formato_hora).time()
    parte_fecha=datetime.strptime(fecha,formato_fecha).date()
    return(datetime.combine(parte_fecha,parte_hora))

# Opción 3 :tener fecha como datatime y realizar el incremento con la hora
def incrementar_date(fecha,hora):
    formato='%Y-%m-%d'
    fecha_date=datetime.strptime(fecha,formato)
    componentes=hora.split(":")
    return fecha_date.__add__(timedelta(minutes=int(componentes[1]),hours=int(componentes[0])))

    


print(unir_fecha_hora(fecha,salida))
print(componer_date_time(fecha,salida))
print(incrementar_date(fecha,salida))








