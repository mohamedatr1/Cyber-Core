<?php
$max_requests = 10;
$time_frame = 10;
$time_block = 60;
$ip = $_SERVER["REMOTE_ADDR"];
$log_file = "log.txt";
$ban_file = "banned_ips.txt";
$now = time(); 
if (file_exists($ban_file)){
    foreach(file($ban_file,FILE_IGNORE_NEW_LINES) as $banned){
        list($banned_ip,$unblock_time) = explode("|",$banned);
        if ($banned_ip === $ip && $now < (int)$unblock_time){
            header("HTTP/1.1 403 Forbidden");
            readfile("block.html");
            exit();
        }
    }
}

$requests = file_exists($log_file) ? array_filter(file($log_file,FILE_IGNORE_NEW_LINES),function($req) use ($ip,$now,$time_frame){
    list($req_ip , $timestamp) = explode("|",$req);
    return $req_ip === $ip && $timestamp > $now - $time_frame;
}) : [];

$requests[] = "$ip|$now";
file_put_contents($log_file, implode(PHP_EOL,$requests). PHP_EOL);

if(count($requests) > $max_requests){
    file_put_contents($ban_file,"$ip | ". ($now + $time_block) . PHP_EOL,FILE_APPEND);
    header("HTTP/1.1 403 Forbidden");
    readfile("block.html");
    exit();
}


echo "<center><h1>Welcome to my site<h1></center>"

?>