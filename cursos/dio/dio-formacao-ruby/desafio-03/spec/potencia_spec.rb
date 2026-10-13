require_relative '../lib/potencia'

RSpec.describe Potencia do
  let(:potencia) { Potencia }

  describe '#calcular' do
    it 'um número positivo' do
      resultado = potencia.calcular(2, 3)
      expect(resultado).to eq(8)
    end

    it 'um número negativo' do
      resultado = potencia.calcular(-2, 3)
      expect(resultado).to eq(-8)
    end

    it 'com expoente zero' do
      resultado = potencia.calcular(5, 0)
      expect(resultado).to eq(1)
    end

    it 'passar um valor inválido como base' do
      expect { potencia.calcular('a', 2) }.to raise_error(NoMethodError)
    end

    it 'passar um valor inválido como expoente' do
      expect { potencia.calcular(2, 'b') }.to raise_error(TypeError)
    end
  end
end
