<?php

if(isset($_POST['submit']) && isset($_FILES['my_image'])){
    echo"<pre>";
    print_r($FILES['image']);
    echo"</pre>";
    
}else{
    header("Location: reservation.php");
}