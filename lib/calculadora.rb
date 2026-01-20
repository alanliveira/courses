class Calculadora
  def somar(valor1, valor2)
    valor1 + valor2
  end

	def subtrair(valor1, valor2)
    valor1 - valor2
	end

	def multiplicar(valor1, valor2)
    valor1 * valor2
	end

	def dividir(valor1, valor2)
    return raise 'Numero não pode ser visivel por 0' if valor2 == 0
		valor1 / valor2
	end
end