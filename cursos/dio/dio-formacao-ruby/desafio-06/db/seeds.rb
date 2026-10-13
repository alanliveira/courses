# This file should ensure the existence of records required to run the application in every environment (production,
# development, test). The code here should be idempotent so that it can be executed at any point in every environment.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Example:
#
#   ["Action", "Comedy", "Drama", "Horror"].each do |genre_name|
#     MovieGenre.find_or_create_by!(name: genre_name)
#   end

livros = [
  { title: "1984", author: "George Orwell", star: 5, description: "Um romance distópico sobre uma sociedade controlada." },
  { title: "O Senhor dos Anéis", author: "J.R.R. Tolkien", star: 5, description: "Uma épica jornada em um mundo de fantasia." },
  { title: "Harry Potter e a Pedra Filosofal", author: "J.K. Rowling", star: 4, description: "A história de um jovem bruxo que descobre seu destino." },
  { title: "O Pequeno Príncipe", author: "Antoine de Saint-Exupéry", star: 5, description: "Uma fábula filosófica sobre a vida e a amizade." },
  { title: "Dom Quixote", author: "Miguel de Cervantes", star: 4, description: "As aventuras de um cavaleiro sonhador e seu fiel escudeiro." },
  { title: "Cem Anos de Solidão", author: "Gabriel García Márquez", star: 5, description: "A saga da família Buendía na mítica cidade de Macondo." },
  { title: "A Revolução dos Bichos", author: "George Orwell", star: 4, description: "Uma alegoria sobre a corrupção do poder." },
  { title: "O Alquimista", author: "Paulo Coelho", star: 4, description: "A jornada de um jovem pastor em busca de seu sonho." },
  { title: "Moby Dick", author: "Herman Melville", star: 3, description: "A obsessão do Capitão Ahab por uma baleia branca." },
  { title: "Guerra e Paz", author: "Liev Tolstói", star: 5, description: "Um retrato épico da sociedade russa durante as guerras napoleônicas." }
]

livros.each do |livro|
  Book.find_or_create_by!(livro)
end
