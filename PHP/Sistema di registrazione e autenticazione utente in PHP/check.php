<?php
    $messageLogin = "Login effettuato con successo";
    $messageError = "Credenziali sbagliate";
    $filename = "registra.csv";
    $handler = fopen($filename, "r");
    $mail = $_POST["mail"];
    $password = $_POST["password"];
    $cookies = $_POST["rimaniLoggato"];
    while($riga = fgetcsv($handler, $length = 0 , $delimiter = ";"))
    {
        if ($riga[2] == $mail and $riga[3] == $password)
        {
            echo "<script type='text/javascript'>alert('$messageLogin');</script>";
            if ($cookies == true)
            {
                setcookie('visita',$mail);
            }
        }else echo "<script type='text/javascript'>alert('$messageError');</script>";
    }