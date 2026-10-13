require_relative 'lib/phone_validator'

print 'Digite um núemro de telefone celular: '
phone = gets.chomp

if Phonevalid?(phone)
  puts 'Número de telefone válido.'
else
  puts 'Número de telefone inválido.'
end
