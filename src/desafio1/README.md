# MLOps Desafio Técnico - Modelagem e API Iris Classifier

## Introdução

Este projeto é uma implementação do Desafio 1, onde o objetivo é desenvolver uma API para classificar flores do dataset Íris(<https://archive.ics.uci.edu/dataset/53/iris>) em suas respectivas espécies com base em características como o comprimento e a largura das sépalas e pétalas.

## Contexto do Desafio

O dataset Íris é amplamente utilizado na comunidade de Machine Learning para tarefas de classificação. Ele inclui três espécies de flores de Íris (_Iris setosa_, _Iris versicolor_ e _Iris virginica_) com 50 amostras cada, onde cada amostra consiste em quatro características e a espécie da flor. O desafio consiste em construir uma API que possa prever a espécie de uma flor de Íris com base nessas características.

## Escolha da Arquitetura e Ferramentas

A arquitetura deste projeto foi projetada para ser simples, mas eficiente, utilizando as seguintes ferramentas:

- **FastAPI**: Escolhido por sua agilidade, performance e suporte fácil para desenvolvimento de APIs REST, além de integração automática com ferramentas de documentação como Swagger.
- **Poetry**: Utilizado para o gerenciamento de dependências. Oferece um controle mais refinado e consistente das bibliotecas utilizadas, além de facilitar a configuração do ambiente.
- **Docker**: Para containerização da aplicação, garantindo que ela seja executada da mesma forma em qualquer ambiente. (assim esperamos =D)
- **Pydantic**: Para validação de dados de entrada e serialização, aproveitando as funcionalidades de type hints do Python para garantir a corretude dos dados.
- **Scikit-learn**: Para treinamento do modelo de classificação das flores de Íris.
- **GitHub Actions**: Para automação de CI/CD, garantindo testes e deploy contínuos e consistentes.

## Pipeline da Modelagem

1. **Distribuição das Classes**: Para visualizar a distribuição das classes nos conjuntos de treinamento e teste.
2. **Métricas do Modelo**: Para visualizar as métricas de avaliação do modelo (acurácia, precisão, recall, f1-score).
3. **Matriz de Confusão**: Para entender como o modelo está classificando corretamente e onde está errando.
4. **Curva ROC**: Para visualizar a performance do modelo em termos de taxa de verdadeiros positivos e falsos positivos.
5. **Importância das Features**: Para entender quais features estão contribuindo mais para as previsões do modelo.
6. **Informações Básicas do Dataset**: Para visualizar a distribuição das features individuais.
7. **Curva de Aprendizado**: Para entender como a performance do modelo muda com o tamanho do conjunto de treinamento.
8. **Validação Cruzada**: Para avaliar a estabilidade do modelo em diferentes subconjuntos de dados.
9. **Treino e Validação**: Treinamento do modelo e avaliação dos resultados.
10. **Plots**: Geração de gráficos para análise visual dos resultados.
11. **Salva Artefatos**: Salvamento do modelo treinado e dos gráficos gerados.

## Configuração do Projeto

### Pré-requisitos

Para rodar este projeto, você precisará ter na sua maquina:

- Python 3.11 (ou o pyenv para gerenciar versoes do python)
- Docker
- Poetry

---

## TESTANDO O PROJETO DESAFIO1 DA MANEIRA RAPIDA E FACIL

## Instalação e Execução

**Forma fácil e mais simples**

1. Clone o repositorio
2. Após garantir que esteja com o **Python 3.11, Docker e Poetry** instalados;
3. Garanta que voce esteja no diretorio RAIZ do projeto: Rode o comando `$pwd` para validar essa etapa.

- `poetry shell`
- `poetry install`

4. Após ter o python instalado, e o ambiente poetry de pé com as dependencias instaladas

- Rode o comando: `make train` para treinar o modelo com algoritmo KNN,a pós garantir a completude do treino...

5. Rode o comando: `make api` para subir a api em localhost
6. Recomendo abrir a api em uma aba do terminal, e em outra aba enviar a requisição para testar a saída do seu endpoint

- **Exemplo de requisições(devem ir 4 parametros na requição post):**

```bash
  - http POST <http://127.0.0.1:8000/iris/predict> sepal_length:=5.1 sepal_width:=3.5 petal_length:=1.4 petal_width:=0.2

  - http POST <http://127.0.0.1:8000/iris/predict> sepal_length:=6.3 sepal_width:=2.8 petal_length:=5.1 petal_width:=1.5

  - http POST <http://127.0.0.1:8000/iris/predict> sepal_length:=7.2 sepal_width:=3.6 petal_length:=6.1 petal_width:=2.5
```

---

## Instalação e Execução

**Utilizando DOcker**

1. **Clonar o Repositório**

   ```bash
   git clone git@github.com:andressamarcal/mlops-desafio-tecnico.git
   cd src/desafio1/
   ```

2. **Usando Docker**

- Construir a imagem Docker:

  `docker build -t iris-classifier-api .`

- Executar o contêiner Docker:

  `docker run -p 8000:8000 iris-classifier-api`

A API estará disponível no endereço <http://127.0.0.1:8000>

**Usando Poetry**

- Instalação de Dependências com Poetry
  `poetry install`

- Executando Localmente
  `poetry run uvicorn api.v1.main:app --reload`

- Uso da API
  Após iniciar o serviço, a API estará disponível em <http://localhost:8000>. Você pode acessar a documentação interativa gerada por Swagger em <http://localhost:8000/docs>, onde é possível testar os endpoints diretamente pelo navegador.

**Reproduzindo a Pipeline**

- Para treinar o modelo e salvar o modelo treinado:
  `poetry run python src/desafio1/models/ml/iris_train.py`

Este comando irá:
1 Carregar o dataset
2 Treinar o modelo com o algoritmo KNN
3 Avaliar o modelo
4 Salvar o modelo treinado no diretório ./saved_models
5 Gerar plots de distribuição de classes, métricas de avaliação e curvas ROC.

**Endpoints da API**

`GET /` : Verifica o status da API.

`POST /iris/predict` : Faz a previsão da espécie de Íris com base nas características fornecidas.

**Parâmetros:**

- sepal_length
- sepal_width
- petal_length
- petal_width

### Exemplo de Uso da API

```bash
http POST <http://127.0.0.1:8000/iris/predict> sepal_length:=5.1 sepal_width:=3.5 petal_length:=1.4 petal_width:=0.2

GET /docs: Acessa a documentação interativa da API.
```

## Boas Práticas Utilizadas

- Versionamento da API: Utilização de roteadores para gerenciar diferentes versões da API.
- Gerenciamento de Dependências: Uso do Poetry para gerenciar dependências e ambientes virtuais.
- Estrutura Modular: Separação clara entre módulos de treino de modelo, ingestão de dados, serviços e roteadores da API.
- Validação de Dados: Utilização do Pydantic para validação dos dados de entrada e saída.
- Manuseio de Exceções: Tratamento de erros e respostas HTTP adequadas para diferentes tipos de exceções.
- Logging e Mensagens de Erro: Utilização de mensagens de log claras e detalhadas para facilitar a auditoria e a depuração.
- Reprodutibilidade de Ambiente usando Docker. O Dockerfile está configurado para instalar todas as dependências necessárias e rodar a API.

**Usando o Poetry:**

`poetry install`

Execute o ambiente virtual:

`poetry shell`

# Avaliação da Eficiência do Projeto

Alguns algoritmos e tecnicas foram avaliados e testados no processo de modelagem:

- Decision Tree (iris_dt_v1_20240626.pkl): Nao foi escolhido.
- Naive Bayes (iris_nb_v1_20240626.pkl): Nao foi escolhido.
- Logistic Regression (iris_lr_v1_20240626.pkl): Nao foi escolhido.
- K-Nearest Neighbors (iris_knn_v1_20240626.pkl): Modelo escolhido

Análisando o Desempenho, e motivando a minha escolha =D

- Decision Tree (DT)

  - Vantagens: Fácil de interpretar e visualizar, capaz de capturar relações não lineares.
  - Desvantagens: Propenso a **overfitting**, especialmente com conjuntos de dados pequenos como o Íris.

- Logistic Regression (LR)

  - Vantagens: Simples, eficiente e bom desempenho com problemas de classificação linear.
  - Desvantagens: Pode ter **desempenho inferior quando as classes não são linearmente separáveis**. No caso do Íris, as classes não são perfeitamente lineares, o que pode limitar o desempenho da regressão logística. =/

- Naive Bayes (NB)
  - Vantagens: Simples, rápido e funciona bem com dados categóricos.
  - Desvantagens: Assumir que todas as features são independentes é uma simplificação que raramente se verifica na prática. No caso do Íris, as **features podem não ser completamente independentes**, o que afeta negativamente o desempenho do Naive Bayes.
  -
- K-Nearest Neighbors (KNN)
  - Vantagens: Não faz suposições sobre a distribuição dos dados, captura relações não lineares entre as features, fácil de entender e implementar.
  - Desvantagens: **Pode ser computacionalmente caro para grandes conjuntos de dados**, mas o conjunto de dados Íris é pequeno, então isso não é um problema significativo.

Maaaaaaas, bora lá, se não ficou claro, vou explicar o pq o KNN foi o melhor =P

- Simplicidade e Eficácia:
  - Para o tamanho do conjunto de dados do Íris (150 amostras), o KNN é uma escolha prática que oferece uma boa acurácia sem a necessidade de um modelo complexo. ;D
- Desempenho Avaliado pelas Métricas:
  - As métricas de avaliação mostram uma precisão, recall e f1-score elevados para o KNN, indicando que ele é capaz de classificar corretamente a maioria das amostras.

> A melhor performance/métricas foi do KNN. Os demais foram identificados problemas com Overfitting =/ e falta de generalização com o conjunto de teste/produtivo.

## Métricas de Avaliação do Modelo

As métricas de avaliação do modelo são:

```bash
Relatório de Classificação:

               precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       0.83      1.00      0.91        10
           2       1.00      0.80      0.89        10

    accuracy                           0.93        30
   macro avg       0.94      0.93      0.93        30
weighted avg       0.94      0.93      0.93        30
```

As métricas acima, indicam que o KNN tem uma alta precisão e recall, especialmente para as classes 0 e 1, mostrando um bom equilíbrio entre os diferentes tipos de erro (falsos positivos e falsos negativos). Com isso, o KNN se mostrou mais eficiente para este problema específico do que os outros modelos testados. =D

<!-- ## Boas Práticas e Padrões de Projeto -->
<!--  -->
<!-- <!-- Este projeto segue as melhores práticas de desenvolvimento de software e padrões de projeto, incluindo: --> -->
<!--  -->
<!-- 1. Use Descriptive Resource URLs -->
<!-- 2. Use HTTP Verbs Correctly -->
<!-- 3. Use Proper HTTP Status Codes -->
<!-- 4. Version Your APIs -->
<!-- 5. Implement Pagination for Large Data Sets -->
<!-- 6. Use Authentication and Authorization -->
<!-- 7. Provide Clear Documentation -->

<!-- - **Modularidade**: O código é organizado em módulos lógicos e arquivos separados para diferentes responsabilidades. -->
<!-- <!-- - **Documentação de Código e API**: O código é amplamente documentado e a API possui documentação interativa gerada pelo Swagger. -->
<!-- <!-- - **Testes Automatizados**: Inclui uma suíte de testes que pode ser executada automaticamente em ambientes de CI/CD. -->
<!-- <!-- - **Práticas de CI/CD**: Integração contínua configurada para garantir que cada commit seja testado e que erros sejam capturados rapidamente. -->
<!-- <!-- - **Segurança e Manutenção**: Uso de contêineres para garantir que a aplicação seja segura e fácil de manter em produção. -->

# Arquitetura do Projeto

Para esse projeto foi escolhida a **Arquitetura em Camadas**:

1 Interface de Apresentação (Presentation Layer):

- **/api**
- Contém a configuração da API, roteadores e os pontos de entrada para os serviços.

2 Camada de Serviço (Service Layer):

- **/api/services**
- Contém a lógica de negócios e regras de serviço.

3 Camada de Domínio (Domain Layer):

- **/models**
- Contém os modelos de machine learning e schemas de dados.

4 Dados estáticos (Static Data):

- **/data**
- Contém gráficos e informações estáticas usadas para análise e treinamento de modelos.

5 Modelos Treinados (Trained Models):

- **/saved_models**
- Contém os arquivos de modelos treinados.

6 Testes (Tests):

- **/tests**
- Contém os testes unitários para verificar a funcionalidade dos serviços e modelos.

```
.
├── api                -> Presentation Layer
│   ├── config.py
│   ├── data_ingestion.py
│   ├── __init__.py
│   ├── services       -> Service Layer
│   │   ├── data_service.py
│   │   ├── prediction_service.py
│   │   └── __init__.py
│   └── v1
│       ├── main.py
│       ├── routers     -> Routing Layer
│       │   ├── iris_router.py
│       │   └── __init__.py
│       ├── __init__.py
├── data                -> Static Data
│   ├── class_distribution.png
│   ├── confusion_matrix.png
│   ├── cross_validation_scores.png
│   ├── dataset_info.png
│   ├── feature_importance.png
│   ├── learning_curve.png
│   ├── model_metrics.png
│   └── roc_curve.png
├── Dockerfile
├── __init__.py
├── models              -> Domain Layer
│   ├── ml              -> Machine Learning Models
│   │   ├── iris_train.py
│   │   └── __init__.py
│   └── schemas         -> Data Schemas
│       ├── iris_schema.py
│       └── __init__.py
├── README.md
├── saved_models        -> Trained Models
│   ├── iris_dt_v1_20240626.pkl
│   ├── iris_knn_v1_20240626.pkl
│   ├── iris_lr_v1_20240626.pkl
│   └── iris_nb_v1_20240626.pkl
└── tests               -> Tests
    ├── __init__.py
    ├── test_data_service.py
    └── test_iris_router.py
```

## Conclusão

Este projeto exemplifica como aplicar boas práticas de engenharia de software na construção
de uma API robusta, escalável e facilmente mantível para a classificação de flores de Íris. A
escolha de FastAPI, Poetry, e Docker foi direcionada para facilitar o desenvolvimento, o
teste e a distribuição da aplicação, garantindo uma implantação eficaz e eficiente. :)
