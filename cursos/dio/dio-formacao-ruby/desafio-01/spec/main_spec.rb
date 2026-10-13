require 'stringio'
require_relative '../main.rb'

RSpec.describe '#main' do
  it 'exibe a mensagem final com os dados informados' do
    input = StringIO.new("Alan\nOliveira\n30\n")
    output = StringIO.new

    main(input: input, output: output)

    expect(output.string).to include(
      "Parabens Alan Oliveira, você foi cadastrado. A sua idade é 30"
    )
  end
end