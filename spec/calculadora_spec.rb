require_relative '../lib/calculadora'

RSpec.describe Calculadora do
  let(:calculadora) { Calculadora.new }

  describe '#somar' do
    it 'soma dois números positivos' do
      resultado = calculadora.somar(10, 5)
      expect(resultado).to eq(15)
    end

    it 'soma números negativos' do
      resultado = calculadora.somar(-10, -5)
      expect(resultado).to eq(-15)
    end

    it 'soma um número positivo com um negativo' do
      resultado = calculadora.somar(10, -5)
      expect(resultado).to eq(5)
    end
  end

  describe '#subtrair' do
    it 'subtrai dois números' do
      resultado = calculadora.subtrair(10, 5)
      expect(resultado).to eq(5)
    end

    it 'subtrai números negativos' do
      resultado = calculadora.subtrair(-10, -5)
      expect(resultado).to eq(-5)
    end
  end

  describe '#multiplicar' do
    it 'multiplica dois números' do
      resultado = calculadora.multiplicar(10, 5)
      expect(resultado).to eq(50)
    end

    it 'multiplica por zero' do
      resultado = calculadora.multiplicar(10, 0)
      expect(resultado).to eq(0)
    end

    it 'multiplica números negativos' do
      resultado = calculadora.multiplicar(-10, -5)
      expect(resultado).to eq(50)
    end
  end

  describe '#dividir' do
    it 'divide dois números' do
      resultado = calculadora.dividir(10, 5)
      expect(resultado).to eq(2)
    end

    it 'lança erro ao dividir por zero' do
      expect { calculadora.dividir(10, 0) }.to raise_error('Numero não pode ser visivel por 0')
    end

    it 'divide números negativos' do
      resultado = calculadora.dividir(-10, -5)
      expect(resultado).to eq(2)
    end
  end
end