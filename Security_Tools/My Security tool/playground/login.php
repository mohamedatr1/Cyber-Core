<?php
$correct_admin = "admin";
$correct_pass = "123456";
if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $user = $_POST["username"];
    $pass = $_POST["password"];
    if ($user == $correct_admin && $pass === $correct_pass){
        echo "Login - Welcome";
    }else{
        echo "Error data";
    }
    
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