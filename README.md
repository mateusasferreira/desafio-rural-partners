# Sobre

API de cadastro de Produtores Rurais.

(Instruções de instalação e dependências para OS Ubuntu 22.04)

# Dependências

[Docker >=27.1.1](https://docs.docker.com/engine/install/ubuntu/)

[Make](https://www.gnu.org/software/make/) (`sudo apt install make`)

# Instruções

1) Buildar a imagem:

```shell
make build
```

2) Executar migrations e seeding:

```shell
make migrate
```

3) Executar testes:

```shell
make test
```

4) Executar o servidor local:

```shell
make run
```

**Acessar a aplicação via `http://localhost:8000`

5) Listar todos os comandos:

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
