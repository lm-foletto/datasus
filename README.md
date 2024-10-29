# Estudo de Caso: Previsão de Internações Hospitalares por Doenças Respiratórias

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Objetivo](#objetivo)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Execução do Projeto](#execução-do-projeto)
- [Treinamento do Modelo](#treinamento-do-modelo)
- [Deploy do Modelo](#deploy-do-modelo)
- [Consumo de Dados do Datasus](#consumo-de-dados-do-datasus)
- [Monitoramento e Observabilidade](#monitoramento-e-observabilidade)
- [Licença](#licença)

## Descrição do Projeto

Este projeto visa prever o número de internações hospitalares relacionadas a doenças respiratórias usando dados históricos e variáveis ambientais (como temperatura e qualidade do ar) fornecidos pelo [DATASUS](https://servicos-datasus.saude.gov.br/). A previsão de internações pode auxiliar gestores hospitalares e autoridades de saúde a alocar recursos, preparar leitos e desenvolver estratégias de prevenção.

[Manual API](https://datasus.saude.gov.br/wp-content/uploads/2022/02/Manual-de-Utilizacao-da-API-e-Sus-Notifica.pdf)

## Objetivo

O principal objetivo é desenvolver um pipeline completo de **Machine Learning** que:
1. Treinar um modelo preditivo usando dados históricos de internações e variáveis ambientais.
2. Implantar a solução em um ambiente de produção utilizando **Docker**.
3. Implementar o sistema de **monitoramento** que permita acompanhar a performance do modelo ao longo do tempo.

## Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:

```plaintext
├── api                 # Código para a API (FastAPI)
│   ├── main.py         # Arquivo principal para execução da API
├── data                # Dados e scripts de ingestão de dados
│   ├── download_data.py # Script para consumir dados do Datasus
├── model               # Modelos e scripts de treinamento
│   ├── preprocess.py   # Pré-processamento de dados
│   ├── train_model.py  # Script de treinamento do modelo
│   ├── model.joblib    # Arquivo do modelo treinado
├── prometheus.yml      # Configurações para monitoramento com Prometheus
├── Dockerfile          # Arquivo Docker para containerizar a aplicação
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação do projeto
```

## Instalação

### Pré-requisitos
- [Docker](https://docs.docker.com/get-docker/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Prometheus](https://prometheus.io/download/)

### Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/lm-foletto/datasus.git
   cd datasus
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução do Projeto

### 1. Ingestão e Pré-processamento dos Dados

Utilize o script `download_data.py` para obter os dados do DATASUS:
```bash
python data/download_data.py
```

### 2. Executando a API

Após treinar o modelo, você pode executar a API com o FastAPI para fazer previsões.

1. Construa a imagem Docker:
   ```bash
   docker build -t hospital-predictor .
   ```

2. Execute o contêiner:
   ```bash
   docker run -p 8000:8000 hospital-predictor
   ```

A API estará disponível em [http://localhost:8000](http://localhost:8000).

## Treinamento do Modelo

1. Execute o script de treinamento:
   ```bash
   python model/train_model.py
   ```
   O modelo treinado será salvo como `model/model.joblib`.

## Deploy do Modelo

Este projeto usa Docker para deploy. O Dockerfile define o ambiente necessário para rodar a API com o modelo.

1. **Construção da Imagem Docker**:
   ```bash
   docker build -t hospital-predictor .
   ```

2. **Execução do Contêiner**:
   ```bash
   docker run -p 8000:8000 hospital-predictor
   ```

Para acessar a documentação da API, navegue até [http://localhost:8000/docs](http://localhost:8000/docs).

## Consumo de Dados do Datasus

Os dados são extraídos do DATASUS via API. O script `download_data.py` automatiza o processo de coleta e armazenamento dos dados no formato necessário para o treinamento do modelo.

Para consumir os dados diretamente do DATASUS:
```bash
python data/download_data.py
```

Este script está configurado para acessar endpoints de interesse e atualizar a base de dados local com novas informações de internações e variáveis ambientais.

## Monitoramento e Observabilidade

Este projeto usa **Grafana** e **Prometheus** para monitorar a performance do modelo em produção.

### Configuração do Prometheus
1. Certifique-se de que o Prometheus está instalado e configurado corretamente.
2. Use o arquivo `prometheus.yml` para definir as métricas de monitoramento do modelo.
3. Inicie o Prometheus:
   ```bash
   prometheus --config.file=prometheus.yml
   ```
### Configuração do Grafana
1. Inicie o Grafana como um contêiner Docker ou instale-o em seu sistema. Para iniciar com Docker, execute:
   ```bash
   docker run -d -p 3000:3000 --name=grafana grafana/grafana
   ```
2. Acesse o Grafana em http://localhost:3000 e faça login (usuário padrão: admin, senha padrão: admin).
3. Configure o Prometheus como fonte de dados:
- Vá até Configuration > Data Sources.
- Selecione Add data source e escolha Prometheus.
- No campo URL, insira http://prometheus:9090.
- Salve a configuração com Save & Test.


### Métricas Monitoradas
- **Taxa de erro**: Taxa de erro das previsões realizadas pelo modelo.
- **Latência**: Tempo médio de resposta da API para cada previsão.
- **Acurácia**: Desempenho do modelo em períodos específicos.

Alertas podem ser configurados no Prometheus para notificar quando houver quedas na precisão do modelo ou aumentos na taxa de erro.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).