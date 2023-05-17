import json
import requests


key = "JCYRKGHRJZwWha9LHlFGyGT4jOmaBwWd"
c_or=input(f"Ingrese ciudad de origen: ")
c_des=input(f"Ingrese ciudad de destino: ")
url = f"http://www.mapquestapi.com/directions/v2/route?key={key}&from={c_or}&to={c_des}"
data = requests.get(url).json()
data2 = requests.get(url).json()
distance = data["route"]["distance"]
segundos = data2["route"]["time"]
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60
print(f"Narrativa del viaje desde {c_or} hasta {c_des}:")
print(f"La Distancia entre {c_or} y {c_des} es de {distance:.2f} kilómetros")
print(f"La Duración del viaje es de {horas} horas, {minutos} minutos, y {segundos} segundos")
salida = input("Presione 'q' para salir: ")
if salida.lower() == "q":
    exit()

