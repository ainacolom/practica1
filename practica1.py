#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

# URL del servicio Open Meteo
api_url = "https://api.open-meteo.com/v1/forecast?latitude=39.56939&longitude=2.65024&hourly=temperature_2m"

try:
    # Consumir la API
    response = requests.get(api_url)
    response.raise_for_status()  # Lanzar error si la respuesta no es 200

    # Extraer las temperaturas
    data = response.json()
    temperatures = data["hourly"]["temperature_2m"]

    # Calcular temperatura media
    avg_temperature = sum(temperatures) / len(temperatures)
    print(f"La temperatura media es: {avg_temperature:.2f}°C")

except (requests.RequestException, KeyError) as e:
    print(f"Error al consumir la API: {e}")

