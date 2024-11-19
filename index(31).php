<?php

$host="localhost";
$user="root";
$pass="";
$db="tracker";
$conn=new mysqli($host,$user,$pass,$db);
if($conn->connect_error){
    echo "Failed to connect DB".$conn->connect_error;
}
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add to shopping cart</title>
    <link rel="stylesheet" href="style1.css">
    <script src="https://kit.fontawesome.com/aa7454d09f.js" crossorigin="anonymous"></script>
  
</head>
<body>

    <!-- Header -->
    <header>
        <div class="leftItem">
            <img src="https://thumbs.dreamstime.com/z/captivating-tableau-financial-insight-unfolds-against-dark-enigmatic-backdrop-vibrant-green-charts-graphs-trace-286564219.jpg">
            <nav class="nav">
                <li class="navLink">Home</li>
                <li class="navLink">About</li>
                <li class="navLink">Financial Track</li>
                <li class="navLink">Reviews</li>
            </nav>
        </div>

        <div class="rightItem">
            <span class="signin">
                <p  style="font-size:15px;">
                    Hello,  <?php 
                    if(isset($_SESSION['userName'])){
                     $userName=$_SESSION['userName'];
                     $query=mysqli_query($conn, "SELECT users.* FROM `users` WHERE users.userName='$userName'");
                     while($row=mysqli_fetch_array($query)){
                         echo $row['userName'];
                     }
                    }
                    ?>
                    </p>
                
                <i class="fas fa-user" id="login-btn"></i>
            </span>
            
            
        </div>
        <form action="" class="login-form">
            
            <a href="http://localhost/log/index.php">logout</a>
              
        </form>
        
    </header>
      
    <main>
        <div id="main">
            <marquee direction=left> <p id="tag"><b>Track, Save, Grow – Your Money, Simplified...!!!</b></p>
                    
            </marquee>
          </div> 
    
        </main>
   
    
    
    <script src="scripts.js" ></script>
    <footer>
        
        
        <div class="foot-pannel4">
            <div class="pages">
                <ul>
                <a>Conditional of Use</a>
                <a>Privacy Notice</a>
                <a>Your Ads Privacy Choices</a>
                <a>Contact us :finance@gmail.com</a>
                </ul>
        </div>
        </div>
        <div class="copyright"></div>    
        
     </footer>
    
   
</body>
</html>