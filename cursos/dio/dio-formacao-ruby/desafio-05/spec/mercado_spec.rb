require_relative '../lib/mercado'
require_relative '../lib/produto'

RSpec.describe Mercado do
  describe 'Inicialização' do
    it 'deve criar um mercado com lista de produtos vazia por padrão' do
      mercado = Mercado.new

      expect(mercado.produtos).to eq([])
    end

    it 'deve criar um mercado com produtos iniciais' do
      produto1 = Produto.new(1, 'Caneta', 2.5)
      produto2 = Produto.new(2, 'Lápis', 1.5)

      mercado = Mercado.new([produto1, produto2])

      expect(mercado.produtos).to include(produto1, produto2)
      expect(mercado.produtos.length).to eq(2)
    end
  end

  describe 'Comprar produto' do
    it 'deve retornar mensagem de sucesso ao comprar um produto disponível' do
      produto = Produto.new(1, 'Caneta', 2.5)
      mercado = Mercado.new([produto])

      resultado = mercado.comprar(produto)

      expect(resultado).to eq('Produto Caneta comprado com sucesso!')
    end

    it 'deve retornar mensagem de indisponibilidade ao tentar comprar produto não disponível' do
      produto_disponivel = Produto.new(1, 'Caneta', 2.5)
      produto_indisponivel = Produto.new(2, 'Lápis', 1.5)
      mercado = Mercado.new([produto_disponivel])

      resultado = mercado.comprar(produto_indisponivel)

      expect(resultado).to eq('Produto Lápis não está disponível no mercado.')
    end

    it 'deve permitir comprar múltiplos produtos disponíveis' do
      produto1 = Produto.new(1, 'Caneta', 2.5)
      produto2 = Produto.new(2, 'Borracha', 1.0)
      mercado = Mercado.new([produto1, produto2])

      resultado1 = mercado.comprar(produto1)
      resultado2 = mercado.comprar(produto2)

      expect(resultado1).to eq('Produto Caneta comprado com sucesso!')
      expect(resultado2).to eq('Produto Borracha comprado com sucesso!')
    end
  end

  describe 'Gerenciamento de produtos' do
    it 'deve permitir adicionar novos produtos à lista' do
      mercado = Mercado.new
      produto = Produto.new(1, 'Caneta', 2.5)

      mercado.produtos << produto

      expect(mercado.produtos).to include(produto)
    end

    it 'deve permitir remover produtos da lista' do
      produto = Produto.new(1, 'Caneta', 2.5)
      mercado = Mercado.new([produto])

      mercado.produtos.delete(produto)

      expect(mercado.produtos).not_to include(produto)
    end
  end
end
