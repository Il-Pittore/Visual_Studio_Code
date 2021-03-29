<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Benvenuto</title>
</head>
<body>
<form>
    <p>Benvenuto!</p>
    <p>Ecco i servizi che puoi sottoscrivere:</p>
    <?php
    if (isset($_COOKIE['cookies']))
    {
        $filename = "servizi.csv";
        $handler = fopen($filename, "r");
        $mail = $_COOKIE['cookies'];
        $riga = fgetcsv($handler, $length = 0 , $delimiter = ";");
    }
    else
    {
        print("Non hai abbonamenti salvati o non hai i cookies salvati <br>Riprova ");
    }
    ?>
</form>
</body>
