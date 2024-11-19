<?php 

include 'connect.php';

if(isset($_POST['signUp'])){
    $userName=$_POST['userName'];
    
    $password=$_POST['password'];
    $retype=$_POST['retype'];
   
    if ($password !== $retype) {
        echo "Passwords do not match.";
        exit;
    }
    $password=md5($password);
     $checkUserName="SELECT * From users where userName='$userName'";
     $result=$conn->query($checkUserName);
     if($result->num_rows>0){
        echo "UserName Already Exists !";
     }
     else{
        $insertQuery="INSERT INTO users(userName,password)
                       VALUES ('$userName','$password')";
            if($conn->query($insertQuery)==TRUE){
                header("location: index.php");
            }
            else{
                echo "Error:".$conn->error;
            }
     }
   

}

if(isset($_POST['signIn'])){
   $userName=$_POST['userName'];
   $password=$_POST['password'];
   $password=md5($password) ;
   
   $sql="SELECT * FROM users WHERE userName='$userName' and password='$password'";
   $result=$conn->query($sql);
   if($result->num_rows>0){
    session_start();
    $row=$result->fetch_assoc();
    $_SESSION['userName']=$row['userName'];
    header("Location:http://localhost/FinancialTracker/index(31).php");
    exit();
   }
   else{
    echo "Not Found, Incorrect Email or Password";
   }

}
?>