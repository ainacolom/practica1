# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Instalar Git
RUN apt-get update && apt-get install -y git

# Crear y establecer directorio de trabajo
WORKDIR /app

# Clonar el repositorio desde GitHub
RUN git clone https://github.com/ainacolom/practica1.git

# Movernos al directorio clonado
WORKDIR /app/practica1

# Instalar dependencias
RUN pip install --no-cache-dir pandas requests

# Ejecutar el script Python
CMD ["python", "practica1.py"]
