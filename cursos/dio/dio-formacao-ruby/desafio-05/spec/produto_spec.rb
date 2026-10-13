require_relative '../lib/produto'

RSpec.describe Produto do
  describe 'Atributos' do
    it 'deve ter id, nome e preco' do
      produto = Produto.new(1, 'Caneta', 2.5)

      expect(produto.id).to eq(1)
      expect(produto.nome).to eq('Caneta')
      expect(produto.preco).to eq(2.5)
    end

    it 'deve permitir alterar nome e preco' do
      produto = Produto.new(1, 'Caneta', 2.5)

      produto.nome = 'Lápis'
      produto.preco = 1.5

      expect(produto.nome).to eq('Lápis')
      expect(produto.preco).to eq(1.5)
    end
  end
end
