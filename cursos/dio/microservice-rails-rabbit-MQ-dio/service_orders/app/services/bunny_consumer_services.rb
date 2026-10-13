class BunnyConsumerServices
  VALID_MODELS = { "User": "Customer" }

  class << self
    def call!(properties, payload)
      return false unless VALID_MODELS.keys.include?(properties[:type].to_sym)

      model_klass(properties[:type].to_sym).create_or_update_from_bunny(JSON.parse(payload))
    end

    def model_klass(type)
      VALID_MODELS[type].constantize
    end
  end
end
