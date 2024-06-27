# mlops-desafio-tecnico

- **Github repository**: <https://github.com/andressamarcal/mlops-desafio-tecnico/>
- **Documentation** <https://andressamarcal.github.io/mlops-desafio-tecnico/>

Projeto contendo as resoluções técnicas e teoricas de **dois desafios**.
Dentro do projeto, você encontrará as resoluções nos seguintes caminhos:

`mlops-desafio-tecnico/src/desafio1`: **Solução para o desafio1 do case técnico.**

`mlops-desafio-tecnico/src/desafio2`: **Solução para o desafio2 do case técnico.**

## TESTANDO O PROJETO DESAFIO1 DA MANEIRA RAPIDA E FACIL

## Instalação e Execução

**Forma fácil e mais simples**

1. Clone o repositorio
2. Após garantir que esteja com o **Python 3.11, Docker e Poetry** instalados;
3. Garanta que voce esteja no diretorio RAIZ do projeto: Rode o comando `$pwd` para validar essa etapa.

- `poetry shell`
- `poetry install`

4. Após ter o python instalado, e o ambiente poetry de pé com as dependencias instaladas

- Rode o comando: `make train` para treinar o modelo com algoritmo KNN,a pós garantir a completude do
  treino...

5. Rode o comando: `make api` para subir a api em localhost
6. Recomendo abrir a api em uma aba do terminal, e em outra aba enviar a requisição para testar a saída
   do seu endpoint

- **Exemplo de requisições(devem ir 4 parametros na requição post):**

```bash
  - http POST <http://127.0.0.1:8000/iris/predict> sepal_length:=5.1 sepal_width:=3.5 petal_length:=1.4
petal_width:=0.2

  - http POST <http://127.0.0.1:8000/iris/predict> sepal_length:=6.3 sepal_width:=2.8 petal_length:=5.1
petal_width:=1.5

  - http POST <http://127.0.0.1:8000/iris/predict> sepal_length:=7.2 sepal_width:=3.6 petal_length:=6.1
petal_width:=2.5
```

---

## Configurando o Projeto com o Docker

1. Baixe o projeto em sua maquina, utilizando o git:
   `git clone git@github.com:andressamarcal/mlops-desafio-tecnico.git`

2. **Certifique-se de estar no diretorio raiz do projeto**, onde encontra-se o arquivo do Dockerfile, após isso, em seguida, rode o comando:
   `docker build -t iris-classifier .`

3. Após a conclusão do Docker build, você pode testar o treinamento do modelo e a API com os seguintes comandos.
   1. **Treinamento do Modelo**
      Para treinar o modelo dentro do contêiner, você pode usar o comando docker run com a tag iris-classifier e especificar o comando
      **make train**:
      `docker run iris-classifier make train`
      Este comando irá executar o processo de treinamento do modelo conforme definido no Makefile.
   1. **Subir a API**
      Para rodar a API, use o comando docker run novamente, mas desta vez especifique o comando **make api**:
      `docker run -p 8000:8000 iris-classifier make api`
      Este comando irá iniciar a API no contêiner e mapear a porta 8000 do contêiner para a porta 8000 do host, permitindo que você acesse a API no endereço <http://localhost:8000>.

# Estrutura do Projeto/Repositorio

```

```
