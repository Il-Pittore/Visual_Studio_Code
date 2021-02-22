<?php
    $var = 11 + "7 nani";
    echo '1) ';
    var_dump($var);
    echo '<br>2) ';
    $valore_intero = 8;
    $valore_intero = (bool)$valore_intero;
    var_dump($valore_intero);
    echo '<br>3) ';
    $vettore = array('colore'=>'giallo', 'mese'=>'luglio', 'stagione'=>'estate');
    $oggetto = (object)$vettore;
    var_dump($oggetto);
    echo '<br>4) ';
    $string_var = "0kldkldslò4lòlsdjljf";
    $int_var = (int)$string_var;
    var_dump($int_var);