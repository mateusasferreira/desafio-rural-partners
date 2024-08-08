# Sobre

API de cadastro de Produtores Rurais.

(Instruções de instalação e dependências para OS Ubuntu 22.04)

# Dependências

[Docker >=27.1.1](https://docs.docker.com/engine/install/ubuntu/)

[Make](https://www.gnu.org/software/make/) (`sudo apt install make`)

# Instruções

1) Criar arquivo .env

```shell
mv .env.example .env
```

2) Buildar a imagem:

```shell
make build
```

3) Executar migrations e seeding:

```shell
make migrate
```

4) Executar testes:

```shell
make test
```

5) Gerar token de autenticação:

```shell
make testtoken
```

Este comando cria um token de API para autenticar nos endpoint, no padrão `Authorization: Token <token>`.
Esse comando foi criado somente para agilizar testes locais, mas também pode ser criado pela interface do admin.

6) Executar o servidor local:

```shell
make run
```

**Acessar a aplicação via `http://localhost:8000`

7) Listar todos os comandos:

```shell
make help
```

# Documentação:

### Endpoints

Documentação de endpoints (swagger) disponível em `http://localhost:8000/docs`

### Admin

Para acessar o admin da aplicação:

1) Criar um superuser com o comando `make superuser`

2) Acessar o admin via `http://localhost:8000/admin`
