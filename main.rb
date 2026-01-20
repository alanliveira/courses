require 'io/console'
require_relative 'lib/calculadora'

options = [
    { id: 1, descricao: 'Somar'         },
    { id: 2, descricao: 'Subtrair'      },
    { id: 3, descricao: 'Multiplicar'   },
    { id: 4, descricao: 'Dividir'       },
    { id: 0, descricao: 'Sair'          },
]

calculadora = Calculadora.new

loop do
  options.each do |option|
    puts "#{option[:id]} - #{option[:descricao]}"
  end

  print "\nDigite a operação desejada: "
  option_selected = gets.chomp.to_i

  break if option_selected == 0
  
  print 'Digite o primeiro número: '
  first_number = gets.chomp.to_f

  print 'Digite o segundo número: '
  second_number = gets.chomp.to_f

  case option_selected
  when 1
    result = calculadora.somar(first_number, second_number)
    puts "\nResultado da soma: #{result}"
  when 2
    result = calculadora.subtrair(first_number, second_number)
    puts "\nResultado da subtração: #{result}"
  when 3
    result = calculadora.multiplicar(first_number, second_number)
    puts "\nResultado da multiplicação: #{result}"
  when 4
    begin
      result = calculadora.dividir(first_number, second_number)
      puts "\nResultado da divisão: #{result}"
    rescue => e
      puts "Erro: #{e.message}"
    end
  else
    puts 'Opção inválida. Tente novamente.'
  end

  print "\nPressione qualquer tecla para continuar..."
  STDIN.getch
  system('clear') || system('cls')
end