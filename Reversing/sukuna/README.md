# flag
SHELL{M3L0v4l3nT_5hR1n3}

# solution

The given file is an elf exe file.
opening it in ghidra and going to main fuction we can see a there is a call for another function named domain_expansion
![main_showing_fun](https://user-images.githubusercontent.com/70768880/118613897-d1792e00-b7dc-11eb-9756-66198e746fe0.png)
jumping to that function we see some hex values i.e.
![shell{](https://user-images.githubusercontent.com/70768880/118614114-0ab19e00-b7dd-11eb-847c-e5ae0c738ee3.png)
this means : "SHELL{" and is stored at < local c8 >
![shrine](https://user-images.githubusercontent.com/70768880/118614132-10a77f00-b7dd-11eb-8a7a-71ccc0781d54.png)
this is : "5hR1n3}" and is stored at < local 88 >
![melvo](https://user-images.githubusercontent.com/70768880/118614148-169d6000-b7dd-11eb-8386-cfe28ba842d9.png)
this is : "M3L0v413" and is stored at <local 48> ( rax )
![nt0](https://user-images.githubusercontent.com/70768880/118614168-1ac97d80-b7dd-11eb-9146-42a47dc75aa9.png)
this is : "nT_" and is stored at <local 40> ( edx )

That is there are 3 variables carrying strings i.e.
first one : "SHELL{"
second one : "5hR1n3}" 
third one : "M3L0v413nT_" 



![concat1](https://user-images.githubusercontent.com/70768880/118614191-2026c800-b7dd-11eb-95b2-8ac56014cd95.png)
here the first and third strings are concatinated and is stored in first i.e.
now there are only two strings left they are :
"SHELL{M3L0v413nT_" and "5hR1n3}"
![concat2](https://user-images.githubusercontent.com/70768880/118614218-24eb7c00-b7dd-11eb-96d1-3217a9d5e311.png)
here the left out two strings are joined and eventually making a flag.
i.e. : SHELL{M3L0v4l3nT_5hR1n3}

![strcmp](https://user-images.githubusercontent.com/70768880/118614250-2cab2080-b7dd-11eb-9549-be5b886bbf07.png)
this is compating the final concatinated string with the given inputed string.


