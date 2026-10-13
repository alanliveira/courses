class BunnyClient
  class << self
    def connect!
      @connection = Bunny.new
      @connection.start

      if @connection.open?
        @channel = @connection.create_channel

        @fan_out = @channel.fanout("users.out")
        @connected = true
      end
    end

    def push(payload, type)
      connect! unless @connected
      @fan_out.publish(payload, { app_id: "users", type: type })

      true
    end
  end
end
