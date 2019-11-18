 function myValidate()
        {
            if(document.getElementById("username").value =="admin" && document.getElementById("password").value =="admin")
            {
                window.location.assign("dashboard.html")
               
                //alert("Login success");
            }
            else
            {
                alert("Invalid Credentials");
            }

        }
   

/*
    var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function myValidate(){
var usr = document.getElementById("username").value;
var pwd = document.getElementById("password").value;
if ( usr == "admin" && pwd == "admin"){
alert ("Login successfully");
window.location = "dashboard.html"; // Redirecting to other page.
return false;
}
else{
attempt --;// Decrementing by one.
alert("You have left "+attempt+" attempt;");
// Disabling fields after 3 attempts.
    if( attempt == 0){
        document.getElementById("username").disabled = true;
        document.getElementById("password").disabled = true;
        document.getElementById("submit").disabled = true;
            return false;
                }
        } 
}
*/