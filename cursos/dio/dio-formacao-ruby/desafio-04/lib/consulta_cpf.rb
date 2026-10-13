require 'cpf_cnpj'

class ConsultaCpf
  def self.call(cpf)
    raise "CPF inválido, verifique se foi digitado corretamente nesse modelo: #{CPF.generate}" unless CPF.valid?(cpf)

    cpf = CPF.new(cpf)
    "CPF digitado é valido: #{cpf.number}"
  end
end
