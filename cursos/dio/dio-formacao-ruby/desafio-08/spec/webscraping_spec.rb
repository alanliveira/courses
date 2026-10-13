require_relative '../lib/webscraping'

RSpec.describe Webscraping do
  describe '.scrape_titles' do
    let(:valid_url) { 'https://example.com' }
    let(:invalid_url) { 'https://invalid-url.com' }

    it 'returns an array of titles from the webpage' do
      titles = Webscraping.scrape_titles(valid_url)
      expect(titles).to be_a(String)
      expect(titles).to include('veja se temos um titulo:')
    end

    it 'handles HTTP errors gracefully' do
      expect do
        Webscraping.scrape_titles(invalid_url)
      end.to output(/redirection forbidden/).to_stdout
    end

    it 'handles other errors gracefully' do
      allow(URI).to receive(:open).and_raise(StandardError.new('Some error'))
      expect do
        Webscraping.scrape_titles(valid_url)
      end.to output(/An error occurred: Some error/).to_stdout
    end
  end
end
