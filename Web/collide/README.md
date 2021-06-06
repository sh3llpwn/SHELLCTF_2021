SHELL{1nj3ct_&_coll1d3_9d25f1cfdeb38a404b6e8584bec7a319}

## Solution:

The name of the challenge is a hint.  
Look at the php source code : 
```php
            $source = show_source("index.php", true);
            echo("<div>");
            print $source;
            echo("</div>");
```
The above code is printing the index.php file. 

On analysisng further 
```php
            if (isset($_GET['shell']) && isset($_GET['pwn'])) {
                if ($_GET['shell'] !== $_GET['pwn'] && hash("sha256", $_GET['shell']) === hash("sha256", $_GET['pwn'])) {
                    include("flag.php");
                    echo("<h1>$flag</h1>");
                } else {
                    echo("<h1>Try harder!</h1>");
                }
            } else {
                echo("<h1>Collisions are fun to see</h1>");
            }
```
1. It checks if variables shell & pwn are set ot not, if not it prints "Collisions are fun to see"
2. If they are set, the inner if statement would print the flag if the values of the two variables are unequal but their SHA1 hash has to be equal. Hence a hash collision.
3. We find two different values that give the same SHA256 hash (not really practical), or else we could exploit the php code but setting the variables as arrays. 
4. Lets give both arrays different values, e.g. with query string ``` ?shell[]=0&pwn[]=1 ```.
5. This way both variables are unequal and since they are arrays, hash function would give the same error status code on both sides of '==='.
6. Hurray! we enter the if block and get the flag. 
