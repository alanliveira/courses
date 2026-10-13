require_relative 'lib/webscraping'

print 'Digite um site para ver qual é o seu título: '
site = gets.chomp

if /\A#{URI::DEFAULT_PARSER.make_regexp(%w[http https])}\z/.match?(site)
  puts 'Site válido!'
else
  puts "Site inválido! Certifique-se de incluir 'http://' ou 'https://'."
  exit
end

webscraper = Webscraping.scrape_titles(site)

puts webscraper
