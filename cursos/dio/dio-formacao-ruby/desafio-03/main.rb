# frozen_string_literal: true

require_relative 'lib/potencia'

puts <<~EOF
                 __                       .__#{'        '}
  ______   _____/  |_  ____   ____   ____ |__|____#{'   '}
  \\____ \\ /  _ \\   __\\/ __ \\ /    \\_/ ___\\|  \\__  \\#{'  '}
  |  |_> >  <_> )  | \\  ___/|   |  \\  \\___|  |/ __ \\_
  |   __/ \\____/|__|  \\___  >___|  /\\___  >__(____  /
  |__|                    \\/     \\/     \\/        \\/#{' '}

EOF

BASE_POTENCIA = 3
numbers = [nil, nil, nil]

number_results = numbers.map.each_with_index do |number, index|
  print "Digite o #{index + 1} numero para calcular a potência: "
  Potencia.calcular(gets.chomp.to_i, BASE_POTENCIA)
end

puts "\nO resultado dos valores elevado à #{BASE_POTENCIA} é: #{number_results.join(', ')}"
