<?php
    session_start();
    $messageLogin = "Login effettuato con successo";
    $messageError = "Credenziali sbagliate";
    $filename = "registra.csv";
    $handler = fopen($filename, "r");
    $mail = $_POST["mail"];
    $password = $_POST["password"];
    while($riga = fgetcsv($handler, $length = 0 , $delimiter = ";"))
    {
        if ($riga[2] == $mail and $riga[3] == md5($password))
        {
            echo "<script type='text/javascript'>alert('$messageLogin');</script>";
            if ($_POST["loggato"] == true)
            {
                echo "<script type='text/javascript'>alert('cookies');</script>";
                setcookie("cookies",$mail,3600);
            }
        }else echo "<script type='text/javascript'>alert('$messageError');</script>";
    }