miArray=[
    {'fecha': '2026-06-14', 'salida': '10:15', 'llegada': '11:25', 
  'duracion': '1h 10min', 'precio': '3.300', 'salidaFutura': False}, 
  {'fecha': '2026-06-14', 'salida': '11:20', 'llegada': '12:30', 
   'duracion': '1h 10min', 'precio': '3.300', 'salidaFutura': False}, 
   {'fecha': '2026-06-14', 'salida': '12:30', 'llegada': '13:40', 
    'duracion': '1h 10min', 'precio': '3.300', 'salidaFutura': True}, 
    {'fecha': '2026-06-14', 'salida': '13:38', 'llegada': '14:48', 
     'duracion': '1h 10min', 'precio': '3.300', 'salidaFutura': True} 
     ]

print(len(miArray), 'elementos')

for elem in miArray:
    if elem['salidaFutura']==True:
        #print(elem['salida'], elem['salidaFutura'])
        print(elem['salida'])