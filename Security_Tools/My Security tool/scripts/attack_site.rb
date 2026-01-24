require 'net/http'
require 'uri'

url = URI.parse("http://localhost/pycyber1/test1.php")

response = Net::HTTP.get_response(url)

puts "Server : #{response.body.force_encoding("utf-8")}"