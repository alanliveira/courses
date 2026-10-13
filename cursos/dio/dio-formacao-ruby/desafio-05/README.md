# Descrição

Criar um código em três arquivos que "conversem" entre si como aprendido nas aulas. Você simulará o ato de escolher e comprar um produto em um mercado

# Desafio

1. No arquivo ``produto.rb``, crie uma classe chamada ``Produto`` com os atributos: ``nome`` e ``preço``.
2. No arquivo ``mercado.rb`` crie uma classe chamada ``Mercado`` que ao ser
inicializada recebe como atributo um objeto da classe ``Produto``.
3. Dentro da classe, crie um método chamado comprar que imprime a
seguinte frase *"Você comprou o produto #{@produto.nome} no valor de
#{@produto.preco}"*
4. No arquivo ``app.rb`` crie uma instância da classe Produto e adicione
valores aos atributos nome e preco. Depois, inicie uma instância da
classe Mercado passando um objeto produto como atributo e para
execute o método comprar.

# Como Usar

## Pré-requisitos

- Ruby 3.4.7 ou superior instalado
- Bundler instalado (`gem install bundle:2.6.9`)

## Instalação

1. Clone ou acesse o diretório do projeto:
```bash
cd dio-formacao-ruby/desafio-05
```

2. Instale as dependências do projeto:
```bash
bundle install
```

## Executando a Calculadora

Para executar o programa da calculadora em modo interativo:

```bash
ruby main.rb
```

## Executando os Testes

O projeto utiliza **RSpec** para testes automatizados. Para executar todos os testes:

```bash
bundle exec rspec
```

Para visualizar o resultado dos testes:

```bash
bundle exec rspec --format documentation
```

