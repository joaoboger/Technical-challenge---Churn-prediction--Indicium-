# Projeto de Previsão de Churn

Este repositório contém código e arquivos relacionados ao projeto de previsão de churn para uma instituição financeira.

## Notebooks

O diretório `notebooks` contém Jupyter notebooks para análise exploratória de dados (EDA) e desenvolvimento de modelos de aprendizado de máquina.

- [churn_eda_ml.ipynb](notebooks/churn_eda_ml.ipynb): Notebook para EDA e desenvolvimento de modelos de ML.

## Pipeline

O diretório `pipeline` contém scripts e arquivos relacionados ao pipeline de previsão de churn.

- [churn_pipeline.py](pipeline/churn_pipeline.py): Script Python para executar o pipeline de previsão de churn e fazer previsões em novos dados.

## Dataset

O diretório `data` armazena o conjunto de dados usado para a previsão de churn.

## Uso

1. Clone o repositório:

```bash
git clone https://github.com/joaoboger/TechnicalChallenge-ChurnPrediction
```

2. Prepare os dados de entrada:
   - Renomeie o arquivo de dados desejado a ser previsto como `Abandono_teste.csv`.
   - Mova o arquivo `Abandono_teste.csv` para o diretório `data` dentro do repositório.
   - Instale as dependências necessárias executando o seguinte comando para instalar a versão específica das bibliotecas:

```bash
pip install -r requirements.txt
```

3. Execute o pipeline de previsão de churn:
   - Abra um terminal ou prompt de comando e navegue até o diretório raiz do repositório clonado.
   - Execute o seguinte comando para executar o script `churn_pipeline.py`:

```bash
python pipeline/churn_pipeline.py
```

4. Verifique as previsões de saída:
   - Após a execução do script, os resultados de churn previstos serão gerados.
   - Localize o arquivo de previsões de saída chamado `predictions.csv`.
   - Encontre o arquivo `predictions.csv` no diretório `output` dentro do repositório.
   - O arquivo terá duas colunas: a primeira coluna representa os números das linhas, e a segunda coluna contém os valores previstos de churn.

