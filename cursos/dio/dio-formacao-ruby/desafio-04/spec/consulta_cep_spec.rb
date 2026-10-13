require_relative '../lib/consulta_cpf'

RSpec.describe ConsultaCpf do
  describe '.call' do
    context 'quando o CPF é válido' do
      it 'retorna a mensagem de CPF válido com a formatação correta, incluindo o CPF formatado' do
        cpf_valido = '688.808.230-00' # Exemplo de CPF válido
        resultado = ConsultaCpf.call(cpf_valido)
        expect(resultado).to eq("CPF digitado é valido: #{cpf_valido}")
      end

      it 'retorna a mensagem de CPF válido com a formatação correta, sem formatação do CPF' do
        cpf_valido = '68880823000' # Exemplo de CPF válido
        resultado = ConsultaCpf.call(cpf_valido)
        expect(resultado).to eq("CPF digitado é valido: #{cpf_valido}")
      end
    end

    context 'quando o CPF é inválido' do
      it 'levanta uma exceção com a mensagem de CPF inválido' do
        cpf_invalido = '123.456.789-00' # Exemplo de CPF inválido
        expect do
          ConsultaCpf.call(cpf_invalido)
        end.to raise_error(RuntimeError, /CPF inválido, verifique se foi digitado corretamente nesse modelo:/)
      end
    end
  end
end
