<!DOCTYPE html>
<html lang="kun">
<?php
    $ide = $pse = "";
    $id = $pa = "";
    $is_Go = true;
    if($_SERVER['REQUEST_METHOD'] == "POST"){
        if(empty($_POST['id'])){
            $ide = "你号呢？没得找管理员要一个!";
            $is_Go = false;
        }
        else{
            $id = $_POST["id"];
        }
        if(empty($_POST['password'])){
            $pse = "密码是错的!认不得密码找管理员查看一下";
            $is_Go = false;
        }
        else{
            $pa = $_POST["password"];
        }

        if($is_Go){
            header("Location: Operating.php");
        }
    }
?>
<head>
	<script>
		function jk(action_to, botton_event, Do){
			var sign;
			sign = [document.getElementById("frot"),document.getElementById("frot1"),document.getElementById("frot5"),
			document.getElementById("frot3"),document.getElementById("frot4")];
			sign[0].setAttribute('action', action_to);
			sign[2].innerHTML = Do;
			sign[4].setAttribute('value', botton_event);
			if(sign[4].value == "注册"){
				sign[4].setAttribute('onclick', 'jk("loginSave.php", "返回", "注册")');
			}
			else{
				sign[4].setAttribute('onclick', 'jk("admin.php", "注册", "登录")');
			}
			
		}
	</script>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
	<title>账号登录</title>
	<style>
		* {
			margin: 0;
			padding: 0;
		}

		body {
			height: 100vh;
			overflow: hidden;
		}

		.表单 {
			width: 60vw;
			display: block;
			margin: auto;
			margin-top: 45vh;
		}

		@font-face {
			font-family: 华体;
			src: url("../华体.ttf");
		}

		.background {
			height: 45vh;
			color: white;
			position: relative;
		}

		video {
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			position: absolute;
			object-fit: fill;
		}

		.box {
			width: 100%;
			height: 100%;
			position: relative;
		}

		.background h1,h2{
			text-align: center;
		}

		.background h1{
			padding-top: 25vh;
			font-size: 60px;
		}

		.background h2{
			font-size: 30px;
		}

		form{
			display: block;
			width: 16%;
			position: relative;
			font-size: 30px;
			margin: auto;
			color: white;
		}
	</style>
</head>

<body>
	<div class="box">
		<!-- autoplay 自动播放  loop循环播放  muted 声音 preload 预加载 -->
		<video autoplay loop preload muted>
			<source src="./back2.mp4">
		</video>
		<div class="background">
			<h1>Welcome</h1>
			<h2>网站管理系统</h2>
		</div>
		<div style="position: relative;">
			<h1 style="text-align: center; color: white; font-size: 35px; margin-bottom: 1vh;" id="frot5">登录</h1>
			<form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF'])?>" method="post" id="frot">
				账号:<span style="color: red; font-size: 10px;">*<?php echo $ide?></span><br>
					<input type="text" name="id" style="width: 300px; height: 3vh;" 
					placeholder="输入您的账号id"/><br>
                密码:<span style="color: red; font-size: 10px;">*<?php echo $pse?></span><br>
					<input type="password" name="password" style="width: 300px; height: 3vh;"
					placeholder="输入您的账号密码"/><br>
				<input type="submit" name="submit" value="登录" id="frot3" style="font-size: 30px; margin-top: 1vh; margin-left: 6vw;"/>
			</form>
		</div>
	</div>
</body>

</html>