require_relative '../lib/phone_validator'

RSpec.describe Phone do
  describe '.valid?' do
    it 'returns true for valid 10-digit phone numbers' do
      expect(Phone.valid?('(12) 3456-7890')).to be true
      expect(Phone.valid?('1234567890')).to be true
    end

    it 'returns true for valid 11-digit phone numbers' do
      expect(Phone.valid?('(12) 34567-8901')).to be true
      expect(Phone.valid?('12345678901')).to be true
    end

    it 'returns false for invalid phone numbers' do
      expect(Phone.valid?('12345')).to be false
      expect(Phone.valid?('abcdefghij')).to be false
      expect(Phone.valid?('(12) 3456-789')).to be false
    end

    it 'ignores non-digit characters' do
      expect(Phone.valid?('+1 (234) 567-8901')).to be true
      expect(Phone.valid?('123-456-7890')).to be true
    end
  end
end
