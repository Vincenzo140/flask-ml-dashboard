# Flask-ML-Dashboard

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-00b0ff?style=for-the-badge&logo=Pydantic&logoColor=white)
![REST API](https://img.shields.io/badge/Rest_API-008080?style=for-the-badge&logo=Rest_API&logoColor=white)

Este repositório contém a implementação de uma API em Flask, focada em análise de dados e aplicações assíncronas. O projeto segue boas práticas de desenvolvimento, segurança e deploy em cloud utilizando Docker.

## Stacks Utilizadas

* **Backend:**
    * [Flask](https://flask.palletsprojects.com/en/3.1.x/): Framework web minimalista para Python.
    * [Flask-RESTX](https://flask-restx.readthedocs.io/en/stable/): Extensão do Flask para criação de APIs RESTful.
    * [Pydantic](https://pydantic-docs.helpmanual.io/): Biblioteca para validação de dados usando type hints.
    * [Rich](https://rich.readthedocs.io/en/stable/): Biblioteca para formatação de texto e saída no terminal.
* **Containerização:**
    * [Docker](https://www.docker.com/): Plataforma para desenvolvimento, entrega e execução de aplicações em containers.
* **Gerenciamento de Dependências:**
    * [Poetry](https://python-poetry.org/): Ferramenta para gerenciamento de dependências e empacotamento de projetos Python.

## Como Rodar o Projeto

### Pré-requisitos

* [Docker](https://www.docker.com/) instalado e em execução.
* [Poetry](https://python-poetry.org/) (opcional, para desenvolvimento local).

### Rodando com Docker Compose

1. Navegue até a pasta `docker` do projeto:

   ```bash
   cd docker
   ```

2. Execute o comando abaixo para construir e iniciar o container:

   ```bash
   docker compose up --build
   ```

   Este comando irá:
   - Construir a imagem Docker da aplicação a partir do Dockerfile na pasta `backend`.
   - Iniciar o container da aplicação.

3. 
### Rotas da API

- **/saudacao** (GET): Retorna uma mensagem de saudação.
- **/soma** (POST): Realiza a soma de dois números. Envie um JSON no corpo da requisição com as chaves `number1` e `number2`. Exemplo:
  
  ```json
  {
    "number1": 10,
    "number2": 5
  }
  ```

### Desenvolvimento Local com Poetry (Opcional)

1. Navegue até a pasta `backend`:

   ```bash
   cd backend
   ```

2. Crie um ambiente virtual com Poetry:

   ```bash
   poetry install
   ```

3. Ative o ambiente virtual:

   ```bash
   poetry shell
   ```

4. Execute a aplicação:

   ```bash
   python main.py
   ```

5. 
## Estrutura do Projeto

- **backend**: Contém o código-fonte da API Flask.
- **Dockerfile**: Define as instruções para construir a imagem Docker.
- **app_factory.py**: Fábrica da aplicação Flask.
- **config.py**: Configurações da API.
- **logger**: Módulo de configuração do logger.
- **main.py**: Ponto de entrada da aplicação.
- **routes**: Contém os arquivos que definem as rotas da API.
- **schemas**: Contém os schemas Pydantic para validação de dados.
- **docker**: Contém os arquivos relacionados ao Docker Compose.
- **compose.yaml**: Define os serviços da aplicação para o Docker Compose.
- **.dockerignore**: Lista os arquivos e diretórios que devem ser ignorados pelo Docker.

