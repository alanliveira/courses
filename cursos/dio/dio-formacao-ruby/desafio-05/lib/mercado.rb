class Mercado
  attr_accessor :produtos, :separado

  def initialize(produtos = [])
    @produtos = produtos
    @separado = []
  end

  def comprar(produto)
    if produtos.include? produto
      separado << produto
      @produtos = @produtos.filter { |p| p != produto }
      "Produto #{produto.nome} comprado com sucesso!"
    else
      "Produto #{produto.nome} não está disponível no mercado."
    end
  end

  def estoque
    produtos.map do |produto|
      puts "ID: #{produto.id} | Nome: #{produto.nome} | Preço: #{produto.preco}"
    end
  end
end
