Num1=input("Enter First number")
Sign=input("Enter the operator :+,-,*,/,%,")
Num2=input("Enter Second Number")


if (Sign== '+'):
    print (int(Num1)+int(Num2))
elif (Sign== "-"): 
    if (int(Num1)>int(Num2)):
        print (int(Num1)-int(Num2)) 
    else:print ("ERROR!")
elif (Sign=='/'):
    if(float(Num1)>float(Num2)):
       try:
        print (float(Num1)/float(Num2))
       except ZeroDivisionError:
        print("Zero Division Error")  
    else:print("ERROR!!")
elif (Sign=='*'):
    print(int(Num1)*int(Num2))
elif (Sign=='%'):
    if (float(Num1)>float(Num2)):
      print(float(Num1)%float(Num2))
    else:print("ERROR!!")
else :print("ERROR!!")



