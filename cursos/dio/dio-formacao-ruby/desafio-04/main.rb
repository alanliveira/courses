require_relative 'lib/consulta_cpf'

puts <<~EOF
    _________                            .__   __           ______________________________
  \\_   ___ \\  ____   ____   ________ __|  |_/  |______    \\_   ___ \\______   \\_   _____/
  /    \\  \\/ /  _ \\ /    \\ /  ___/  |  \\  |\\   __\\__  \\   /    \\  \\/|     ___/|    __)#{'  '}
  \\     \\___(  <_> )   |  \\\\___ \\|  |  /  |_|  |  / __ \\_ \\     \\___|    |    |     \\#{'   '}
   \\______  /\\____/|___|  /____  >____/|____/__| (____  /  \\______  /____|    \\___  /#{'   '}
          \\/            \\/     \\/                     \\/          \\/              \\/#{'    '}

EOF

begin
  print 'Digite o valor do CPF que deseja validar (deve conter 11 digitos e pode conter pontos e traço): '
  cpf_input = gets.chomp

  resultado = ConsultaCpf.call(cpf_input)
  puts resultado
rescue StandardError => e
  puts e.message
end
