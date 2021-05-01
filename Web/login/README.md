SHELL{th1s_i5_th3_wa7_845ad42f4480104b698c1e168d29b739}

## Solution:

1. On opening the challenge we see a login box asking for username & password.

2. Examining the source code, the page uses main.js file and the two input variables are fed to the **checkIt()** function when login button is clicked.

3. Lets have a look at the .js file, we see the function checkIt() and a lot of utility functions that look like they are used to calculate MD5 hash. 

4. In the check it function : 
```javascript
function checkIt() {
  var user = document.getElementById("username").value; var pass = document.getElementById("password").value;
  if (user != "din_djarin11") alert("Only for user: din_djarin11"); else {
    var md5 = MD5(pass);
    if (md5 == "855fb2d9397498af693ddb7f09350596") window.location = "./" + pass; 
    else alert("Invalid login");
  }
}
```
> The value of username and password is storedin variables user and pass respectively. 
> If the username entered is "din_djarin11", we calculate the hash of the password input by user. 
> If the hash matches "9ef71a8cd681a813cfd377817e9a08e5", a file with the same name as the password is opened. 
> So if we get the password, we get the flag. 

5. We paste the hash in https://crackstation.net/ and get the password : ir0nm4n

6. Loging in with these creds gives the flag hurray. 
