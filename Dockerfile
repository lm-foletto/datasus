# Dockerfile
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /DATASUS

# Copia os arquivos do projeto para o contêiner
COPY . /DATASUS

# Instala as dependências
RUN pip install -r requirements.txt

# Exponha a porta da API
EXPOSE 8000

# Comando para rodar a aplicação (ajustando o caminho do arquivo main.py na pasta api)
CMD ["uvicorn", "data.main:app", "--host", "0.0.0.0", "--port", "8000"]
