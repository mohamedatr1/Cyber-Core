<?php
$correct_admin = "admin";
$correct_pass = "123456";
# حفظ IP الشخص الذي يقوم باختراق موقعي
$ip =   $_SERVER["REMOTE_ADDR"];

$file = "attemps.json";
# تحقق من وجود الملف اذا لم يكن موجود انشئه
# اذا كان موجود اعمل ديكود واحصل على محتواه
$attemps_data = file_exists($file) ? json_decode(file_get_contents($file),true) : [];
# اذا لم تجد داخل الملف ip  ضف ip
if (!isset($attemps_data[$ip])){
    $attemps_data[$ip] = 0;   
}
# اذا كانت عدد المحاولات اكبر من او يساوي 3 وقف
if($attemps_data[$ip] >= 3){
    die("<center><h1>You are Blocked</h1></center>");
}

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $user = $_POST["username"];
    $pass = $_POST["password"];


if ($user == $correct_admin && $pass === $correct_pass){
    echo "Login - Welcome";
    $attemps_data[$ip] = 0;
}   
else{
    $attemps_data[$ip] += 1;
    echo "Error data";
}
    file_put_contents($file,json_encode($attemps_data));
}

?>


<center>
    <form method="POST">
        <h1>Login Page</h1>
        <input type="text" name="username" placeholder = "Enter Username "><br><br>
        <input type="password" name="password" placeholder = "Enter password"><br><br>
        <button type = "submit">Login Now</button>
        
    </form>
</center>