# Utilizar una imagen base de Python 3.10 basada en Alpine Linux
FROM python:3.10-alpine

# Instalar Git
RUN apk add --no-cache git

# Clonar el repositorio en el directorio /ajedrez-2024-abenavidezUM
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-abenavidezUM.git ajedrez-2024-abenavidezUM

# Establecer el directorio de trabajo
WORKDIR /ajedrez-2024-abenavidezUM

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar las pruebas de cobertura y luego el juego
CMD ["sh", "-c", "coverage run -m unittest discover test && coverage report -m && python main.py"]
