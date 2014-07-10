<!DOCTYPE html>
<html>
<head>
<title>Title</title>

</head>
<body>



<?php
$DNA = escapeshellcmd($_POST['DNA']);

echo shell_exec('./transcribe "'.$DNA.'"');
echo shell_exec('./translate "'.$DNA.'"');
?>




</body>

</html>