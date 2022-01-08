function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
} 
function displaySighnUp() {
  var x = document.getElementById("form2");
    
    x.style.display = "block";
    var y=document.getElementById("msform");
    y.style.display = "none";
  }
function displaylogin(){
 var x = document.getElementById("form2"); 
    x.style.display = "none";
    y=document.getElementById("msform");
    y.style.display = "block";
}