use LWP::UserAgent;
use HTTP::Request;

my $url = "http://localhost/pycyber1/test2.php";
my $user_agent = LWP::UserAgent->new;
my $response = $user_agent->get($url);

if($response->is_success){
    print "Server :".$response->decoded_content
}