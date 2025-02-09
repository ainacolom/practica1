#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

# URL del servicio Open-Meteo
url = "https://api.open-meteo.com/v1/forecast?latitude=39.56939&longitude=2.65024&hourly=temperature_2m"

# Hacer la solicitud GET a la API
response = requests.get(url)

# Verificar si la respuesta fue exitosa
if response.status_code == 200:
    data = response.json()
    temperatures = data['hourly']['temperature_2m']
    average_temp = sum(temperatures) / len(temperatures)
    print(f"Temperatura media en Palma: {average_temp:.2f} °C")
else:
    print("Error al obtener datos de la API")


