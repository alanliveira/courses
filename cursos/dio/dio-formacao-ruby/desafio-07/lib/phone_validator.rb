module Phone
  def self.valid?(phone)
    phone = phone.gsub(/\D/, '')
    pattern = /\d{10,11}/
    !!(phone =~ pattern)
  end
end
