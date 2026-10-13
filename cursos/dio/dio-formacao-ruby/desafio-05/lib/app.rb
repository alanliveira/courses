require_relative 'mercado'
require_relative 'produto'

produto1 = Produto.new(1, 'Caderno', 15.0)
produto2 = Produto.new(2, 'Mochila', 120.0)
produto3 = Produto.new(3, 'Estojo', 25.0)

produtos = [produto1, produto2, produto3]

mercado = Mercado.new(produtos)

puts "Escolhido: id #{produto1.id} | Nome: #{produto1.nome} | Preço: #{produto1.preco}"
puts mercado.comprar(produto1)
puts ''
puts 'Estoque atual:'
puts ''
puts mercado.estoque
