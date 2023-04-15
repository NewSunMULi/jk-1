<?php
    if($_SERVER["PHP_SELF"] == "http://kmjysm.cn/index.php"){
        header("Location: index2.html");
    }
    elseif($_SERVER["PHP_SELF"] == "http://admin.kmjysm.cn/index.php"){
        header("Location: admin.html");
    }
    elseif($_SERVER["PHP_SELF"] == "http://study.kmjysm.cn/index.php"){
        header("Location: index3.html");
    }
    exit();
