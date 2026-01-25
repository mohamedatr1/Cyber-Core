<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
        $sercho = $_POST["search"];
        // echo "<p>".$sercho."</p>";
        // الحماية:
        $security = htmlspecialchars($sercho,ENT_QUOTES,'UTF-8'); #استغناء عن رموز javascript والمسافات..]
        echo "<p>".$security."</p>";
        // الحقنة:
        // <script>alert("XSS FOUND");</script>
}
?>
<!-- الموقع: -->

<form method="POST" >
    <input type="text" name="search" placeholder = "search about">
    <button type = "submit">Search</button>    
</form> 

