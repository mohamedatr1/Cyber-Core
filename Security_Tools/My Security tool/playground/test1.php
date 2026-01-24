    <?php
    $blocked_agent = [
        
        "ruby","python","perl","bot","nmap","curl"

    ];
    $user_agent = strtolower($_SERVER["HTTP_USER_AGENT"] ?? '');
    
    foreach($blocked_agent as $agent){
        if (strpos($user_agent,$agent) !== false){
            die("[+]Access Denied !! ".htmlspecialchars($user_agent));
        }
    }

    echo "<center><h1>Welcome to learn Cyber</h1></center>";
    ?>