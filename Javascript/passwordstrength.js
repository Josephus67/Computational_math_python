/*
let password= "#Bigjoe67";
    if(password.length>=8){
       console.log("first requirement has been met");
    }
    else{
        console.log("first requirement has not been met");
    }
       for(i in password){
            if(password[i]=='#' || password[i]=='!' || password[i]=='@' || password[i]=='$'){
                console.log("Your password contains a symbol");
            }
            else{console.log("Your password doesn't contain a symbol");}
       }
            if(password[i]==1||password[i]==2||password[i]==3||password[i]==4||password[i]==5||password[i]==6||password[i]==7||password[i]==8||password[i]==9){
                console.log("Your password has at least one number")
            }
            else{console.log("your password does not include a number")}
   */ 
  computerChoice='';
  function randNum(){
    num= Math.random();
    if (num<0.34 && num >0){
        computerChoice = 'rock'
    } else if (num>=0.3 && num<0.67){
        computerChoice='paper'
    } else if (num>= 0.67 && num<1){
        computerChoice='scissors'
    }
    return computerChoice;
  }
  console.log(randNum());
    