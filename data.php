<?php
	$server = "localhost";
	$name = "moisensordata";
	$pass = "admin";
	$datab = "moisensor";
	$conn = new mysqli($server,$name,$pass,$datab);
	
	if($conn->connect_error){
		die("connect fail".$conn->connect_error);
		}
	$result1 = $conn->query("SELECT * FROM recenttime1, moirecent10;");
	echo "<h1  style='text-align:center;color: white;'>ข้อมูล sensor ความชื้นตัวที่ 1 ล่าสุด</h1>";
	echo "<table border='2' align=center style='background-color:white'><tr>
	<th style='background-color:white'>วันและเวลา</th></th>
	<th style='background-color:white'>ข้อมูล</th>
	</tr>";
	
	while($row = mysqli_fetch_array($result1))
	{
	echo "<tr>";
	echo "<td style='background-color:white'>" . $row['datet'] . "</td>";
	echo "<td style='background-color:white'>" . $row['data'] . "</td>";
	echo "</tr>";
	}
	echo "</table>";
	
	$result2 = $conn->query("SELECT * FROM recenttime1, moirecent20;");
	
	echo "<h1  style='text-align:center;color: white;'>ข้อมูล sensor ความชื้นตัวที่ 2 ล่าสุด</h1>";
	echo "<table border='2' align=center style='background-color:white'><tr>
	<th style='background-color:white'>วันและเวลา</th>
	<th style='background-color:white'>ข้อมูล</th>
	</tr>";
	
	while($row = mysqli_fetch_array($result2))
	{
	echo "<tr>";
	echo "<td style='background-color:white'>" . $row['datet'] . "</td>";
	echo "<td style='background-color:white'>" . $row['data'] . "</td>";
	echo "</tr>";
	}
	echo "</table>";
	
	$result3 = $conn->query("SELECT * FROM recenttime1, moirecent30;");
	echo "<h1  style='text-align:center;color: white;'>ข้อมูล sensor วัดปุ๋ย ล่าสุด</h1>";
	echo "<table border='2' align=center style='background-color:white'><tr>
	<th style='background-color:white'>วันและเวลา</th>
	<th style='background-color:white'>ข้อมูล</th>
	</tr>";
	
	while($row = mysqli_fetch_array($result3))
	{
	echo "<tr>";
	echo "<td style='background-color:white'>" . $row['datet'] . "</td>";
	echo "<td style='background-color:white'>" . $row['data'] . "</td>";
	echo "</tr>";
	}
	echo "</table>";

?>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="5">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<style>
	*{
		text-align= center;
		background-color: #00989A;
		
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
	<a href="http://192.168.1.2/index1.php">back</a>
	<a href="http://192.168.1.2/data2.php">ไปที่ข้อมูล 1 ชั่วโมงที่แล้ว</a>
	<a href="http://192.168.1.2/data3.php">ไปที่ข้มมูล 2 ชัวโมงที่แล้ว</a>
	<a href="http://192.168.1.2/data4.php">ไปที่ข้มมูล 3 ชัวโมงที่แล้ว</a>
</body>
</html>
