def main(input: $stdin, output: $stdout)
  output.puts <<~EOF
    ____    _    ____    _    ____ _____ ____   ___  
    / ___|  / \\  |  _ \\  / \\  / ___|_   _|  _ \\ / _ \\ 
  | |     / _ \\ | | | |/ _ \\ \\___ \\ | | | |_) | | | |
  | |___ / ___ \\| |_| / ___ \\ ___) || | |  _ <| |_| |
    \\____/_/   \\_\\____/_/   \\_\\____/ |_| |_| \\_\\\\___/                                                     
  EOF

  output.puts ""

  output.print "Adicione o seu primeiro nome: "
  first_name = input.gets.chomp

  output.print "Adicione o seu sobrenome: "
  last_name = input.gets.chomp

  output.print "Adicione a sua idade: "
  age = input.gets.chomp

  output.puts ""
  output.puts "Parabens #{first_name} #{last_name}, você foi cadastrado. A sua idade é #{age}"
end