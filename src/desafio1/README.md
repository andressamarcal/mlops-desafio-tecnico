# MLOps Desafio Técnico - Iris Classifier

## Introdução

Este projeto é uma implementação do Desafio 1, onde o objetivo é desenvolver uma API para classificar flores do dataset Íris em suas respectivas espécies com base em características como o comprimento e a largura das sépalas e pétalas.

## Contexto do Desafio

O dataset Íris é amplamente utilizado na comunidade de Machine Learning para tarefas de classificação. Ele inclui três espécies de flores de Íris (_Iris setosa_, _Iris versicolor_ e _Iris virginica_) com 50 amostras cada, onde cada amostra consiste em quatro características e a espécie da flor. O desafio consiste em construir uma API que possa prever a espécie de uma flor de Íris com base nessas características.

## Escolha da Arquitetura e Ferramentas

A arquitetura deste projeto foi projetada para ser simples, mas eficiente, utilizando as seguintes ferramentas:

- **FastAPI**: Escolhido por sua performance superior e suporte fácil para desenvolvimento de APIs REST, além de integração automática com ferramentas de documentação como Swagger.
- **Poetry**: Utilizado para o gerenciamento de dependências e embalagem do projeto. Oferece um controle mais refinado e consistente das bibliotecas utilizadas, além de facilitar a configuração do ambiente.
- **Docker**: Para containerização da aplicação, garantindo que ela seja executada da mesma forma em qualquer ambiente.
- **Pydantic**: Para validação de dados de entrada e serialização, aproveitando as funcionalidades de type hints do Python para garantir a corretude dos dados.
- **Scikit-learn**: Para treinamento do modelo de classificação das flores de Íris.
- **GitHub Actions**: Para automação de CI/CD, garantindo testes e deploy contínuos e consistentes.

## Pipeline da Modelagem
1. Distribuição das Classes: Para visualizar a distribuição das classes nos conjuntos de treinamento e teste.

2. Métricas do Modelo: Para visualizar as métricas de avaliação do modelo (acurácia, precisão, recall, f1-score).

   Matriz de Confusão: Para entender como o modelo está classificando corretamente e onde está errando.

   Curva ROC: Para visualizar a performance do modelo em termos de taxa de verdadeiros positivos e falsos positivos.

   Importância das Features: Para entender quais features estão contribuindo mais para as previsões do modelo.

   Informações Básicas do Dataset: Para visualizar a distribuição das features individuais.

   Curva de Aprendizado: Para entender como a performance do modelo muda com o tamanho do conjunto de treinamento.

   Validação Cruzada: Para avaliar a estabilidade do modelo em diferentes subconjuntos de dados.

3. Treino e Validação
4. Plots
5. Salva artefatos (modelo, plots)

## Configuração do Projeto

### Pré-requisitos

Para rodar este projeto, você precisará ter o Python 3.11 e o Docker instalados em seu ambiente.

### Instalação e Execução

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/seuusuario/iris-classifier.git
   cd iris-classifier
   ```

Usando Docker

Construir a imagem Docker:

bash
Copiar código
docker build -t iris-classifier-api .
Executar o contêiner Docker:

bash
Copiar código
docker run -p 8000:8000 iris-classifier-api
A API estará disponível no endereço http://127.0.0.1:8000.

Usando Poetry (Alternativa)

Instalação de Dependências com Poetry

bash
Copiar código
poetry install
Executando Localmente

bash
Copiar código
poetry run uvicorn api.v1.main:app --reload
Uso da API
Após iniciar o serviço, a API estará disponível em http://localhost:8000. Você pode acessar a documentação interativa gerada por Swagger em http://localhost:8000/docs, onde é possível testar os endpoints diretamente pelo navegador.

Reproduzindo a Pipeline
Para treinar o modelo e salvar o modelo treinado:

bash
Copiar código
poetry run python src/desafio1/models/ml/iris_train.py
Este comando irá carregar o dataset, treinar o modelo de Regressão Logística, avaliar o modelo, salvar o modelo treinado no diretório ./saved_models e gerar plots de distribuição de classes, métricas de avaliação e curvas ROC.

Endpoints da API
GET /: Verifica o status da API.

POST /iris/predict: Faz a previsão da espécie de Íris com base nas características fornecidas.

Parâmetros: sepal_length, sepal_width, petal_length, petal_width

Exemplo:

bash
Copiar código
http POST http://127.0.0.1:8000/iris/predict sepal_length:=5.1 sepal_width:=3.5 petal_length:=1.4 petal_width:=0.2
GET /docs: Acessa a documentação interativa da API.

Boas Práticas Utilizadas
Versionamento da API: Utilização de roteadores para gerenciar diferentes versões da API.
Gerenciamento de Dependências: Uso do Poetry para gerenciar dependências e ambientes virtuais.
Estrutura Modular: Separação clara entre módulos de treino de modelo, ingestão de dados, serviços e roteadores da API.
Validação de Dados: Utilização do Pydantic para validação dos dados de entrada e saída.
Manuseio de Exceções: Tratamento de erros e respostas HTTP adequadas para diferentes tipos de exceções.
Logging e Mensagens de Erro: Utilização de mensagens de log claras e detalhadas para facilitar a auditoria e a depuração.
Reprodutibilidade de Ambiente
Usando Docker
Para garantir a reprodutibilidade do ambiente, utilize Docker para construir e executar a aplicação. O Dockerfile está configurado para instalar todas as dependências necessárias e rodar a API.

Construir a imagem Docker:

bash
Copiar código
docker build -t iris-classifier-api .
Executar o contêiner Docker:

bash
Copiar código
docker run -p 8000:8000 iris-classifier-api
Usando Poetry (Alternativa)
Para garantir a reprodutibilidade do ambiente usando Poetry:

Instale o Poetry:

Siga as instruções no site oficial do Poetry.

Instale as dependências:

bash
Copiar código
poetry install
Execute o ambiente virtual:

bash
Copiar código
poetry shell
Avaliação da Eficiência do Projeto
O projeto foi desenvolvido seguindo boas práticas de MLOps para garantir a eficiência e a reprodutibilidade. A utilização do FastAPI permite uma API rápida e eficiente. O modelo de Regressão Logística foi escolhido pela sua simplicidade e eficiência, especialmente em conjuntos de dados menores como o Íris.

Métricas de Avaliação do Modelo
As métricas de avaliação do modelo são:

Acurácia: 97%
Precisão: 97%
Recall: 96%
F1-Score: 97%
Eficiência do Projeto
O projeto é eficiente devido às seguintes razões:

Modelo Simples e Eficiente: A Regressão Logística oferece uma boa interpretação dos dados e uma eficiência computacional alta.
Desempenho da API: O FastAPI oferece uma alta performance com uma interface de desenvolvimento intuitiva.
Automatização e Reprodutibilidade: Scripts de treinamento e inicialização da API garantem que o processo possa ser facilmente reproduzido em diferentes ambientes.
Conclusão
Este projeto exemplifica como aplicar boas práticas de engenharia de software na construção de uma API robusta, escalável e facilmente mantível para a classificação de flores de Íris. A escolha de FastAPI, Poetry, e Docker foi direcionada para facilitar o desenvolvimento, o teste e a distribuição da aplicação, garantindo uma implantação eficaz e eficiente.

---

Este projeto é uma implementação do Desafio 1, onde o objetivo é desenvolver uma API para classificar flores do dataset Íris em suas respectivas espécies com base em características como o comprimento e a largura das sépalas e pétalas.

## Contexto do Desafio

O dataset Íris é amplamente utilizado na comunidade de Machine Learning para tarefas de classificação. Ele inclui três espécies de flores de Íris (_Iris setosa_, _Iris versicolor_ e _Iris virginica_) com 50 amostras cada, onde cada amostra consiste em quatro características e a espécie da flor. O desafio consiste em construir uma API que possa prever a espécie de uma flor de Íris com base nessas características.

## Escolha da Arquitetura e Ferramentas

A arquitetura deste projeto foi projetada para ser simples, mas eficiente, utilizando as seguintes ferramentas:

- **FastAPI**: Escolhido por sua performance superior e suporte fácil para desenvolvimento de APIs REST, além de integração automática com ferramentas de documentação como Swagger.
- **Poetry**: Utilizado para o gerenciamento de dependências e embalagem do projeto. Oferece um controle mais refinado e consistente das bibliotecas utilizadas, além de facilitar a configuração do ambiente.
- **Docker**: Para containerização da aplicação, garantindo que ela seja executada da mesma forma em qualquer ambiente.
- **Pydantic**: Para validação de dados de entrada e serialização, aproveitando as funcionalidades de type hints do Python para garantir a corretude dos dados.
- **Scikit-learn**: Para treinamento do modelo de classificação das flores de Íris.
- **GitHub Actions**: Para automação de CI/CD, garantindo testes e deploy contínuos e consistentes.

## Configuração do Projeto

### Pré-requisitos

Para rodar este projeto, você precisará ter o Python 3.9 ou superior e o Docker instalados em seu ambiente.

### Instalação e Execução

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/seuusuario/iris-classifier.git
   cd iris-classifier
   ```

2. **Instalação de Dependências com Poetry**

   ```bash
   poetry install
   ```

3. **Executando Localmente**

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

4. **Usando Docker**

   ```bash
   docker build -t iris-classifier .
   docker run -p 8000:8000 iris-classifier
   ```

### Uso da API

Após iniciar o serviço, a API estará disponível em `http://localhost:8000`. Você pode acessar a documentação interativa gerada por Swagger em `http://localhost:8000/docs`, onde é possível testar os endpoints diretamente pelo navegador.

## Boas Práticas e Padrões de Projeto

Este projeto segue as melhores práticas de desenvolvimento de software e padrões de projeto, incluindo:

1. Use Descriptive Resource URLs
2. Use HTTP Verbs Correctly
3. Use Proper HTTP Status Codes
4. Version Your APIs
5. Implement Pagination for Large Data Sets
6. Use Authentication and Authorization
7. Provide Clear Documentation

- **Modularidade**: O código é organizado em módulos lógicos e arquivos separados para diferentes responsabilidades.
- **Documentação de Código e API**: O código é amplamente documentado e a API possui documentação interativa gerada pelo Swagger.
- **Testes Automatizados**: Inclui uma suíte de testes que pode ser executada automaticamente em ambientes de CI/CD.
- **Práticas de CI/CD**: Integração contínua configurada para garantir que cada commit seja testado e que erros sejam capturados rapidamente.
- **Segurança e Manutenção**: Uso de contêineres para garantir que a aplicação seja segura e fácil de manter em produção.

# Boas Práticas Utilizadas

Versionamento da API: Utilização de roteadores para gerenciar diferentes versões da API.
Gerenciamento de Dependências: Uso do Poetry para gerenciar dependências e ambientes virtuais.
Estrutura Modular: Separação clara entre módulos de treino de modelo, ingestão de dados, serviços e roteadores da API.
Validação de Dados: Utilização do Pydantic para validação dos dados de entrada e saída.
Manuseio de Exceções: Tratamento de erros e respostas HTTP adequadas para diferentes tipos de exceções.
Logging e Mensagens de Erro: Utilização de mensagens de log claras e detalhadas para facilitar a auditoria e a depuração.

## Conclusão

Este projeto exemplifica como aplicar boas práticas de engenharia de software na construção de uma API robusta, escalável e facilmente mantível para a classificação de flores de Íris. A escolha de FastAPI, Poetry, e Docker foi direcionada para facilitar o desenvolvimento, o teste e a distribuição da aplicação, garantindo

uma implantação eficaz e eficiente.

---

# MLOps Desafio Técnico - Iris Classifier

## Introdução

Este projeto é uma implementação do Desafio 1, onde o objetivo é desenvolver uma API para classificar flores do dataset Íris em suas respectivas espécies com base em características como o comprimento e a largura das sépalas e pétalas.

## Contexto do Desafio

O dataset Íris é amplamente utilizado na comunidade de Machine Learning para tarefas de classificação. Ele inclui três espécies de flores de Íris (_Iris setosa_, _Iris versicolor_ e _Iris virginica_) com 50 amostras cada, onde cada amostra consiste em quatro características e a espécie da flor. O desafio consiste em construir uma API que possa prever a espécie de uma flor de Íris com base nessas características.

## Escolha da Arquitetura e Ferramentas

A arquitetura deste projeto foi projetada para ser simples, mas eficiente, utilizando as seguintes ferramentas:

- **FastAPI**: Escolhido por sua performance superior e suporte fácil para desenvolvimento de APIs REST, além de integração automática com ferramentas de documentação como Swagger.
- **Poetry**: Utilizado para o gerenciamento de dependências e embalagem do projeto. Oferece um controle mais refinado e consistente das bibliotecas utilizadas, além de facilitar a configuração do ambiente.
- **Docker**: Para containerização da aplicação, garantindo que ela seja executada da mesma forma em qualquer ambiente.
- **Pydantic**: Para validação de dados de entrada e serialização, aproveitando as funcionalidades de type hints do Python para garantir a corretude dos dados.
- **Scikit-learn**: Para treinamento do modelo de classificação das flores de Íris.
- **GitHub Actions**: Para automação de CI/CD, garantindo testes e deploy contínuos e consistentes.

## Configuração do Projeto

### Pré-requisitos

Para rodar este projeto, você precisará ter o Python 3.11 e o Docker instalados em seu ambiente.

### Instalação e Execução

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/seuusuario/iris-classifier.git
   cd iris-classifier
   Usando Docker
   ```

Construir a imagem Docker:

bash
Copiar código
docker build -t iris-classifier-api .
Executar o contêiner Docker:

bash
Copiar código
docker run -p 8000:8000 iris-classifier-api
A API estará disponível no endereço http://127.0.0.1:8000.

Usando Poetry (Alternativa)

Instalação de Dependências com Poetry

bash
Copiar código
poetry install
Executando Localmente

bash
Copiar código
poetry run uvicorn api.v1.main:app --reload
Uso da API
Após iniciar o serviço, a API estará disponível em http://localhost:8000. Você pode acessar a documentação interativa gerada por Swagger em http://localhost:8000/docs, onde é possível testar os endpoints diretamente pelo navegador.

Reproduzindo a Pipeline
Para treinar o modelo e salvar o modelo treinado:

bash
Copiar código
poetry run python src/desafio1/models/ml/iris_train.py
Este comando irá carregar o dataset, treinar o modelo de Regressão Logística, avaliar o modelo, salvar o modelo treinado no diretório ./saved_models e gerar plots de distribuição de classes, métricas de avaliação e curvas ROC.

Endpoints da API
GET /: Verifica o status da API.

POST /iris/predict: Faz a previsão da espécie de Íris com base nas características fornecidas.

Parâmetros: sepal_length, sepal_width, petal_length, petal_width

Exemplo:

bash
Copiar código
http POST http://127.0.0.1:8000/iris/predict sepal_length:=5.1 sepal_width:=3.5 petal_length:=1.4 petal_width:=0.2
GET /docs: Acessa a documentação interativa da API.

Boas Práticas Utilizadas
Versionamento da API: Utilização de roteadores para gerenciar diferentes versões da API.
Gerenciamento de Dependências: Uso do Poetry para gerenciar dependências e ambientes virtuais.
Estrutura Modular: Separação clara entre módulos de treino de modelo, ingestão de dados, serviços e roteadores da API.
Validação de Dados: Utilização do Pydantic para validação dos dados de entrada e saída.
Manuseio de Exceções: Tratamento de erros e respostas HTTP adequadas para diferentes tipos de exceções.
Logging e Mensagens de Erro: Utilização de mensagens de log claras e detalhadas para facilitar a auditoria e a depuração.
Reprodutibilidade de Ambiente
Usando Docker
Para garantir a reprodutibilidade do ambiente, utilize Docker para construir e executar a aplicação. O Dockerfile está configurado para instalar todas as dependências necessárias e rodar a API.

Construir a imagem Docker:

bash
Copiar código
docker build -t iris-classifier-api .
Executar o contêiner Docker:

bash
Copiar código
docker run -p 8000:8000 iris-classifier-api
Usando Poetry (Alternativa)
Para garantir a reprodutibilidade do ambiente usando Poetry:

Instale o Poetry:

Siga as instruções no site oficial do Poetry.

Instale as dependências:

bash
Copiar código
poetry install
Execute o ambiente virtual:

bash
Copiar código
poetry shell
Avaliação da Eficiência do Projeto
O projeto foi desenvolvido seguindo boas práticas de MLOps para garantir a eficiência e a reprodutibilidade. A utilização do FastAPI permite uma API rápida e eficiente. O modelo de Regressão Logística foi escolhido pela sua simplicidade e eficiência, especialmente em conjuntos de dados menores como o Íris.

Métricas de Avaliação do Modelo
As métricas de avaliação do modelo são:

Acurácia: 97%
Precisão: 97%
Recall: 96%
F1-Score: 97%
Eficiência do Projeto
O projeto é eficiente devido às seguintes razões:

Modelo Simples e Eficiente: A Regressão Logística oferece uma boa interpretação dos dados e uma eficiência computacional alta.
Desempenho da API: O FastAPI oferece uma alta performance com uma interface de desenvolvimento intuitiva.
Automatização e Reprodutibilidade: Scripts de treinamento e inicialização da API garantem que o processo possa ser facilmente reproduzido em diferentes ambientes.
Conclusão
Este projeto exemplifica como aplicar boas práticas de engenharia de software na construção de uma API robusta, escalável e facilmente mantível para a classificação de flores de Íris. A escolha de FastAPI, Poetry, e Docker foi direcionada para facilitar o desenvolvimento, o teste e a distribuição da aplicação, garantindo uma implantação eficaz e eficiente.
"""

Saving the content to README.md
file_path = "/mnt/data/README.md"
with open(file_path, "w") as file:
file.write(readme_content)

file_path
