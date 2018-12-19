<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<title>index</title>
<link href="shiba.css" rel="stylesheet" type="text/css">
</head>

<body>
<div class="header">
    <p class="txt2">SUCCESSFULLY UPLOADED. PROCEED?</p>
</div>
<a href="result.html" class="button" style="top: 400px;">Go on!</a>
</body>
</html>

<?php
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["File"]["name"]);
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
    if(isset($_POST["submit"])) {
        $check = getimagesize($_FILES["File"]["tmp_name"]);
        if($check !== false) {
            $uploadOk = 1;
        } else {
            $uploadOk = 0;
        }
    }
?>
