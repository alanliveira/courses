class Produto
  attr_accessor :id, :nome, :preco

  def initialize(id, nome, preco)
    @id = id
    @nome = nome
    @preco = preco
  end
end
