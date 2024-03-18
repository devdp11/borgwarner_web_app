# Use a imagem oficial do Python
FROM python:3.9-slim

WORKDIR /usr/src/app

# upgrade pip
RUN python -m pip install --upgrade pip

COPY . .
# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
