Total challenges list:
1. flag : SHELL{bas1c_r3v}
## solution
After downloading the file, open it in ghidra.
### step 1:
Go to the main fuction.
![checkflaghighlighted](https://user-images.githubusercontent.com/70768880/116676862-23d8e300-a9c5-11eb-8371-d7a09a9c0f9d.png)
here we can see the there is a call for checkflag function.
### step 2:
Go to the checkflag functions.
![finalflag](https://user-images.githubusercontent.com/70768880/116676941-3b17d080-a9c5-11eb-920f-a346516c0d50.png)
here we can directly see the flag. i.e. SHELL{bas1c_r3v}.

or just by doing strings on the exe file we get the flag.
