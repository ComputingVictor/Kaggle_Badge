# Usamos la imagen base oficial de Python 3.11
FROM python:3.11

# Argumentos para las versiones de Chrome y Chromedriver
ARG CHROME_VERSION="latest"
ARG CHROMEDRIVER_VERSION="latest"

# Instalamos dependencias necesarias para agregar repositorios HTTPS
RUN apt-get update && apt-get install -y wget gnupg2 software-properties-common

# Agregamos la llave GPG oficial de Google
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Agregamos el repositorio de Google Chrome a nuestras fuentes
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Actualizamos el índice de paquetes e instalamos Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable


# Instalamos Chromedriver
RUN apt-get install -yqq unzip \
    && wget -O /tmp/chromedriver.zip  http://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Copiamos el archivo de requisitos primero para aprovechar la caché de Docker layer
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
RUN pip install webdriver-manager --upgrade
RUN pip install packaging

# Copiamos el resto del código de la aplicación
COPY . /app
WORKDIR /app

CMD ["tail", "-f", "/dev/null"]