# Usar una imagen base de Python
FROM python:3.10

# Instalar dependencias
RUN pip install redis

# Instalar Redis en el contenedor
RUN apt-get update && apt-get install -y redis-server

# Definir el comando de inicio: Primero Redis, luego el servidor
CMD redis-server & python server.py
