# Descrição

Criar um projeto utilizando Ruby on Rails

# Desafio

Utilizando todos os conhecimentos que aprendemos em aula,
agora você irá criar o seu blog sozinho, e ele será um blog dos
livros que você leu esse ano, e nele você deverá colocar as
seguintes informações:
1. Título do livro;
2. Autor do livro;
3. Nota que você deu a esse livro;
4. Descrição do livro;

# Como Usar

## Pré-requisitos

- Ruby 3.4.7 ou superior instalado
- Nodejs 24.11.1 ou superior 
- Bundler instalado (`gem install bundle:2.6.9`)
- Yarn 1.22.22

## Instalação

1. Clone ou acesse o diretório do projeto:
```bash
cd dio-formacao-ruby/desafio-06
```

2. Instale as dependências do projeto:
```bash
bundle install
yarn install
```

3. Crie o banco de daos

```bash
bin/rails db:migrate db:seed
```

## Executando ao projeto

Para subir a aplicação você precisa executar o comando:

```bash
bin/dev
```
