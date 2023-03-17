<?php
	$server = "localhost";
	$name = "techno";
	$pass = "admin";
	$datab = "TECHNOFRAM";
	$conn = new mysqli($server,$name,$pass,$datab);
	
	if($conn->connect_error){
		die("connect fail".$conn->connect_error);
		}
	if($_POST['open1']){
	$conn->query("UPDATE ALELAY SET ALELAY1=0 WHERE id = 1;");
	$conn->query("UPDATE status101 SET status = 'open' WHERE id =1; ");
	echo '<script type="text/javascript">';
    echo 'alert("OPEN LELAY1")';
    echo '</script>';
	}
	if($_POST['close1']){
	$conn->query("UPDATE ALELAY SET ALELAY1=1 WHERE id = 1;");
	$conn->query("UPDATE status101 SET status = 'close' WHERE id =1; ");
	echo '<script type="text/javascript">';
    echo 'alert("CLOSE LELAY1")';
    echo '</script>';
	}
	if($_POST['open2']){
	$conn->query("UPDATE ALELAY SET ALELAY1=0 WHERE id = 2;");
	$conn->query("UPDATE status101 SET status = 'open' WHERE id =2; ");
	echo '<script type="text/javascript">';
    echo 'alert("OPEN LELAY2")';
    echo '</script>';
	}
	if($_POST['close2']){
	$conn->query("UPDATE ALELAY SET ALELAY1=1 WHERE id = 2;");
	$conn->query("UPDATE status101 SET status = 'close' WHERE id =2; ");
	echo '<script type="text/javascript">';
    echo 'alert("CLOSE LELAY2")';
    echo '</script>';
	}
	if($_POST['open3']){
	$conn->query("UPDATE ALELAY SET ALELAY1=0 WHERE id = 3;");
	$conn->query("UPDATE status101 SET status = 'open' WHERE id =3; ");
	echo '<script type="text/javascript">';
    echo 'alert("OPEN LELAY3")';
    echo '</script>';
	}
	if($_POST['close3']){
	$conn->query("UPDATE ALELAY SET ALELAY1=1 WHERE id = 3;");
	$conn->query("UPDATE status101 SET status = 'close' WHERE id =3; ");
	echo '<script type="text/javascript">';
    echo 'alert("CLOSE LELAY3")';
    echo '</script>';
	}
	if($_POST['open4']){
	$conn->query("UPDATE ALELAY SET ALELAY1=0 WHERE id = 4;");
	$conn->query("UPDATE status101 SET status = 'open' WHERE id =4; ");
	echo '<script type="text/javascript">';
    echo 'alert("OPEN LELAY4")';
    echo '</script>';
	}
	if($_POST['close4']){
	$conn->query("UPDATE ALELAY SET ALELAY1=1 WHERE id = 4;");
	$conn->query("UPDATE status101 SET status = 'close' WHERE id =4; ");
	echo '<script type="text/javascript">';
    echo 'alert("CLOSE LELAY4")';
    echo '</script>';
	}
	if($_POST['open5']){
	$conn->query("UPDATE ALELAY SET ALELAY1=0 WHERE id = 5;");
	$conn->query("UPDATE status101 SET status = 'open' WHERE id =5; ");
	echo '<script type="text/javascript">';
    echo 'alert("OPEN LELAY5")';
    echo '</script>';
	}
	if($_POST['close5']){
	$conn->query("UPDATE ALELAY SET ALELAY1=1 WHERE id = 5;");
	$conn->query("UPDATE status101 SET status = 'close' WHERE id =5; ");
	echo '<script type="text/javascript">';
    echo 'alert("CLOSE LELAY5")';
    echo '</script>';
	}	
	if($_POST['open6']){
	$conn->query("UPDATE ALELAY SET ALELAY1=0 WHERE id = 6;");
	$conn->query("UPDATE status101 SET status = 'open' WHERE id =6; ");
	echo '<script type="text/javascript">';
    echo 'alert("OPEN LELAY6")';
    echo '</script>';
	}
	if($_POST['close6']){
	$conn->query("UPDATE ALELAY SET ALELAY1=1 WHERE id = 6;");
	$conn->query("UPDATE status101 SET status = 'close' WHERE id =6; ");
	echo '<script type="text/javascript">';
    echo 'alert("CLOSE LELAY6")';
    echo '</script>';
	}
		$result = $conn->query("SELECT * FROM status101");

	echo "<table border='2' align=center style='background-color:white'>
	<tr>
	<th style='background-color:white'>หมายเลข LeLay</th>
	<th style='background-color:white'>สถานะ</th>
	</tr>";

	while($row = mysqli_fetch_array($result))
	{
	echo "<tr>";
	echo "<td style='background-color:white'>" . $row['id'] . "</td>";
	echo "<td style='background-color:white'>" . $row['status'] . "</td>";
	echo "</tr>";
	}
	echo "</table>";
	
	
			
?>
<html>
<head>
<meta charset="UTF-8">	
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<style>
	*{
		text-align:center;
		background-color: #00989A;
		}
	input{
		border-radius: 12px;
		background-color: white;
		}
	a{
		border:2px solid black;
		border-radius: 5px;
		text-decoration: none;
		background-color: white;
		color: black;
  
		}
	
</style>
<body>
<h1><b>ควบคุมอุปกรณ์ OUTPUT<b></h1>

<form method='POST' action="">
	<h1>Lelay1</h1>
	<input type='submit' value='open' name='open1'>
	<input type='submit' value='close' name = 'close1'><br>
	<h1>Lelay2</h1>
	<input type='submit' value='open' name='open2'>
	<input type='submit' value='close' name = 'close2'><br>
	<h1>Lelay3</h1>
	<input type='submit' value='open' name='open3'>
	<input type='submit' value='close' name = 'close3'><br>
	<h1>Lelay4</h1>
	<input type='submit' value='open' name='open4'>
	<input type='submit' value='close' name = 'close4'><br>
	<h1>Lelay5</h1>
	<input type='submit' value='open' name='open5'>
	<input type='submit' value='close' name = 'close5'><br>
	<h1>Lelay6</h1>
	<input type='submit' value='open' name='open6'>
	<input type='submit' value='close' name = 'close6'><br><br><br>
	

</form>
	<a href="http://192.168.1.2/index1.php">back</a>
</body>
</html>
