# Usar una imagen base de Python
FROM python:3.9-slim

# Instalar Git para clonar el repositorio
RUN apt-get update && apt-get install -y git

# Definir directorio de trabajo dentro del contenedor
WORKDIR /app

# Clonar el repositorio de GitHub
RUN git clone https://github.com/ainacolom/practica1.git

# Establecer el directorio del proyecto
WORKDIR /app/practica1

# Instalar dependencias si es necesario
RUN pip install pandas requests

# Ejecutar el script principal
CMD ["python", "practica1.ipynb"]
