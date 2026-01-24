    <?php
    echo "<center><h1>Welcome to learn Cyber</h1></center>";
    
    $ip = "\nip : ".$_SERVER["REMOTE_ADDR"];
    $user = "\nSystem and Browser : ".$_SERVER["HTTP_USER_AGENT"];
    $filoo = fopen("1.txt","a");
    fwrite($filoo,$ip);
    fwrite($filoo,$user);
    fclose($filoo)
    
    ?>