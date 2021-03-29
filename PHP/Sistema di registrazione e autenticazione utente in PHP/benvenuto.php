<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Benvenuto</title>
</head>
<body>
<form>
    <p>Benvenuto!</p>
    <p>Ecco i servizi che hai sottoscritto:</p>
    <?php
    if (isset($_COOKIE['cookies']))
    {
        $filename = "abbonamenti.csv";
        $handler = fopen($filename, "r");
        $mail = $_COOKIE['cookies'];
        while ($riga = fgetcsv($handler, $length = 0 , $delimiter = ";"))
        {
            if ($riga[0] == $mail)
            {
                $sottoscrizioni = $riga;
            }
        }
        foreach ($sottoscrizioni as $item)
        {
            if ($item != $mail)
            {
                print($item);
                print('<br>');
            }
        }
    }
    else
    {
        print("Non hai abbonamenti salvati o non hai i cookies salvati <br>Riprova ");
    }
    ?>

</form>
</body>
