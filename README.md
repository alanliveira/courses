# Descrição

Criar um programa na linguagem de programação Ruby que dê ao usuário uma lista de escolhas que leve a saída  o cálculo escolhido por ele.

# Desafio

Você precisa criar uma calculadora que dê ao usuário um meno de escolha: 1 - soma, 2 - subtração, 3 - Multiplicação, 4 - Divisão, 0 - Sair

# Como Usar

## Pré-requisitos

- Ruby 2.7 ou superior instalado
- Bundler instalado (`gem install bundler`)

## Instalação

1. Clone ou acesse o diretório do projeto:
```bash
cd dio-formacao-ruby-02
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

Ao executar, você verá um menu com as seguintes opções:
- **1** - Somar dois números
- **2** - Subtrair dois números
- **3** - Multiplicar dois números
- **4** - Dividir dois números
- **0** - Sair do programa

### Exemplo de Uso:
```
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
0 - Sair

Digite a operação desejada: 1
Digite o primeiro número: 10
Digite o segundo número: 5

Resultado da soma: 15
```

## Executando os Testes

O projeto utiliza **RSpec** para testes automatizados. Para executar todos os testes:

```bash
bundle exec rspec
```

Para executar os testes com mais detalhes (verbose):

```bash
bundle exec rspec -v
```

Para executar um arquivo de teste específico:

```bash
bundle exec rspec spec/calculadora_spec.rb
```

Para executar testes com um padrão específico:

```bash
bundle exec rspec spec/calculadora_spec.rb -e "somar"
```

### Cobertura de Testes

Os testes cobrem os seguintes cenários:

- **Soma**: positivos, negativos e mista
- **Subtração**: números positivos e negativos
- **Multiplicação**: positivos, negativos, por zero e com zero
- **Divisão**: divisão normal, números negativos e validação de divisão por zero

Para visualizar o resultado dos testes:

```bash
bundle exec rspec --format documentation
```

