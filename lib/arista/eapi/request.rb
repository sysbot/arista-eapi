module Arista
  module EAPI
    class Request
      attr_accessor :switch, :commands, :options, :verify_ssl

      def initialize(switch, commands, options = {}, verify_ssl=true)
        options[:format] ||= 'json'

        self.switch = switch
        self.commands = commands
        self.options = options
        self.verify_ssl = verify_ssl
      end

      def payload
        @payload ||= JSON.generate({
          :jsonrpc => '2.0',
          :method  => 'runCmds',
          :id      => 1,
          :params  => {
            :version => 1,
            :cmds    => commands,
            :format  => options[:format]
          },
        })
      end

      def execute
        req = RestClient::Resource.new(
          switch.url,
          payload,
          :verify_ssl       =>  self.verify_ssl
        )
        Arista::EAPI::Response.new(commands, req.post)
      end
    end
  end
end
