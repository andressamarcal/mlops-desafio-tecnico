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

## Conclusão

Este projeto exemplifica como aplicar boas práticas de engenharia de software na construção de uma API robusta, escalável e facilmente mantível para a classificação de flores de Íris. A escolha de FastAPI, Poetry, e Docker foi direcionada para facilitar o desenvolvimento, o teste e a distribuição da aplicação, garantindo

uma implantação eficaz e eficiente.
