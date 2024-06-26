# mlops-desafio-tecnico

Projeto contendo as resoluções técnicas e teoricas de dois desafios.
Dentro do projeto, você encontrará as resoluções nos seguintes caminhos:

`mlops-desafio-tecnico/src/desafio1`: **Solução para o desafio1 do case técnico.**
`mlops-desafio-tecnico/src/desafio2`: **Solução para o desafio2 do case técnico.**

- **Github repository**: <https://github.com/andressamarcal/mlops-desafio-tecnico/>
- **Documentation** <https://andressamarcal.github.io/mlops-desafio-tecnico/>

## Configurando o Projeto

1. Baixe o projeto em sua maquina, utilizando o git:
   `git clone git@github.com:andressamarcal/mlops-desafio-tecnico.git`

2. **Certifique-se de estar no diretorio raiz do projeto**, onde encontra-se o arquivo do Dockerfile, após isso, em seguida, rode o comando:
   `docker build -t iris-classifier .`

3. Após a conclusão do Docker build, você pode testar o treinamento do modelo e a API com os seguintes comandos.
   1. **Treinamento do Modelo**
      Para treinar o modelo dentro do contêiner, você pode usar o comando docker run com a tag iris-classifier e especificar o comando **make train**:
      `docker run iris-classifier make train`
      Este comando irá executar o processo de treinamento do modelo conforme definido no Makefile.
   1. **Subir a API**
      Para rodar a API, use o comando docker run novamente, mas desta vez especifique o comando **make api**:
      `docker run -p 8000:8000 iris-classifier make api`
      Este comando irá iniciar a API no contêiner e mapear a porta 8000 do contêiner para a porta 8000 do host, permitindo que você acesse a API no endereço http://localhost:8000.

Verificar o Treinamento e a API
Verificar Logs do Treinamento:
Após rodar o comando de treinamento, você deve ver logs indicando o progresso e conclusão do treinamento, bem como onde os gráficos e o modelo foram salvos.

Verificar API:
Após subir a API, você pode acessar a documentação interativa em http://localhost:8000/docs e testar os endpoints disponíveis.

# Estrutura do Projeto/Repositorio

```

.
├── Dockerfile
├── LICENSE
├── Makefile
├── mkdocs.yml
├── mlops_desafio_tecnico
│   ├── api
│   │   ├── v1  # Versionamento da API
│   │   │   ├── __init__.py
│   │   │   ├── main.py  # Ponto de entrada da aplicação FastAPI para a versão 1
│   │   │   ├── dependencies.py  # Gerenciamento de dependências da API
│   │   │   ├── routers  # Roteadores FastAPI
│   │   │       ├── __init__.py
│   │   │       └── iris_router.py  # Roteador para as previsões de íris
│   │   ├── common  # Componentes comuns entre diferentes versões
│   │   │   ├── __init__.py
│   │   │   ├── models.py  # Modelos de dados Pydantic
│   │   │   └── schemas.py  # Schemas para validação de dados
│   │   ├── auth  # Autenticação e autorização
│   │   │   ├── __init__.py
│   │   │   └── auth_handler.py  # Manipulação de autenticação JWT
│   │   └── services  # Serviços de negócio
│   │       ├── __init__.py
│   │       ├── prediction_service.py  # Serviços de predição
│   │       └── data_service.py  # Serviços para manipulação de dados
│   ├── tests  # Testes
│   │   ├── __init__.py
│   │   └── test_iris_router.py
│   └── __init__.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── docs  # Documentação MkDocs
│   ├── index.md
│   └── modules.md
└── .github  # Configuração CI/CD
    └── workflows
        └── ci.yml


```
