require 'nokogiri'
require 'open-uri'

class Webscraping
  def self.scrape_titles(url)
    html = URI.open(url)
    doc = Nokogiri::HTML(html)

    "veja se temos um titulo: #{doc.css('h1').map(&:text).join(', ')}"
  rescue OpenURI::HTTPError => e
    puts "Failed to retrieve the webpage: #{e.message}"
  rescue StandardError => e
    puts "An error occurred: #{e.message}"
  end
end
