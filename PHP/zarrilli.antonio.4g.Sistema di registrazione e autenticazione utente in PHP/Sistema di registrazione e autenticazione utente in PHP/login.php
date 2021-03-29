<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
<form action = "check.php" method = "post">
    <input type='text' name="mail" placeholder="Mail"> <br>
    <input type='password' name="password" placeholder="Password"> <br>
    <input type="checkbox" id="rimaniLoggato" name="loggato">
    <label for="rimaniLoggato"> Resta loggato </label> <br>
    <input type='submit' value="Login">
    <p>Se non hai un'accoult creane uno <br> <button formaction="registra.html">Crea un'account</button> </p>
    <?php
        if (isset($_COOKIE['cookies']))
        {
            echo "<script type='text/javascript'>alert('ciao');</script>";
        }
    ?>

</form>
</body>
