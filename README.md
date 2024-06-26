# mlops-desafio-tecnico

Projeto contendo as resoluções técnicas e teoricas

- **Github repository**: <https://github.com/andressamarcal/mlops-desafio-tecnico/>
- **Documentation** <https://andressamarcal.github.io/mlops-desafio-tecnico/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:andressamarcal/mlops-desafio-tecnico.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

# ARQUITETURA DO PROJETO

```
.
├── Dockerfile
├── LICENSE
├── Makefile
├── mkdocs.yml
├── mlops_desafio_tecnico
│ ├── api
│ │ ├── v1 # Versionamento da API
│ │ │ ├── init.py
│ │ │ ├── main.py # Ponto de entrada da aplicação FastAPI para a versão 1
│ │ │ ├── dependencies.py # Gerenciamento de dependências da API
│ │ │ ├── routers # Roteadores FastAPI
│ │ │ │ ├── init.py
│ │ │ │ └── iris_router.py # Roteador para as previsões de íris
│ │ ├── common # Componentes comuns entre diferentes versões
│ │ │ ├── init.py
│ │ │ ├── models.py # Modelos de dados Pydantic
│ │ │ └── schemas.py # Schemas para validação de dados
│ │ ├── auth # Autenticação e autorização
│ │ │ ├── init.py
│ │ │ └── auth_handler.py # Manipulação de autenticação JWT
│ │ └── services # Serviços de negócio
│ │ ├── init.py
│ │ ├── prediction_service.py # Serviços de predição
│ │ └── data_service.py # Serviços para manipulação de dados
│ ├── tests # Testes
│ │ ├── init.py
│ │ └── test_iris_router.py
│ └── init.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── docs # Documentação MkDocs
│ ├── index.md
│ └── modules.md
└── .github # Configuração CI/CD
└── workflows
└── ci.yml
```

Repository initiated with [fpgmaas/cookiecutter-poetry](<https://github.com/fpgmaas/>
cookiecutter-poetry).
