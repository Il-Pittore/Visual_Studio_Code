<?php
    $filename = 'registra.csv';
    $handler = fopen($filename, 'a');
    $nome = $_POST["username"];
    $cognome = $_POST["surname"];
    $mail = $_POST["mail"];
    $password = md5($_POST["password"]);
    $dati = [$nome,$cognome,$mail,$password];
    fputcsv($handler, $dati, ';');
    fclose($handler);
    echo "<script type='text/javascript'>alert('Registrazione effetuata');</script>";
    include "login.php";