#This is a new program in which students will be given grade according to their marks in grade subject(all the problem are fixed)
Morralscience = int(input("Entre your marks in Moralscience :- "))
Generalknowledge = int(input("Entre your marks in Generalknowledge :- "))
Hindi = int(input("Entre your marks in Hindi :- "))
Drawing = int(input("Entre your marks in Drawing:- "))
Computer = int(input("Entre your marks in Computer :-" ))
totalmarks = (Morralscience+Generalknowledge+Hindi+Drawing+Computer)
print("Your total marks are ---> "+ str(totalmarks))
if(Morralscience==50): 
    print("You got 'A' grade in Moralscience")
elif(50>=Morralscience>=40):
    print("You got 'B' grade in Moral science")
elif(40>=Morralscience>=30):
    print("You got 'C' grade in Moralscience")
elif(30>=Morralscience>=20):
     print("You got 'D' garde in Moralscience")
elif(20>=Morralscience>=10):
    print("You are 'Fail' in Moralscence")
elif(Morralscience>50):
    print("Invalid marks are entered in Moralscience")
elif(10>=Generalknowledge>-1):
    print("You are 'Fail' in Moralscence") 
if(Generalknowledge==50):
    print("You got 'A' grade in Generalknowledge")
elif(50>=Generalknowledge>=40):
    print("You got 'B' grade in Gneralknowledge")
elif(40>=Generalknowledge>=30):
    print("You got 'C' grade in Gneralnowledge")
elif(30>=Generalknowledge>=20):
    print("You got 'D' grade in Generalknowledge")
elif(20>=Generalknowledge>=10):
    print("You are 'Fail' in Generalknowledge")
elif(Generalknowledge>50):
    print("Invalid marks are entered in Generalknowledge")
else:
    print("You are 'Fail' in Generalknowledge")
if(Hindi==50):
    print("You got 'A' grade in Hindi")
elif(50>=Hindi>=40):
    print("You got 'B' grade Hindi")
elif(40>=Hindi>=30):
    print("You got 'C' grade in Hindi")
elif(30>Hindi>20):
    print("You got 'D' grade in Hindi ")
elif(20>=Hindi>=10):
    print("You are 'Fail in Hindi")
elif(Hindi>50):
    print("Invalid marks are entered in Hindi")
else:
    print("You are Fail in Hindi") 
if(Drawing==50):
    print("You got 'A' grade in Drawing")
elif(50>=Drawing>=40):
    print("You got 'B' grade in Drawing")
elif(40>=Drawing>=30):
    print("You got 'C' grade in Drawing")
elif(30>=Drawing>=20):
    print("You got 'D' grade in Drawng")
elif(Drawing>50):
    print("Invalid marks are entered in Drawing")
else:
    print("You are 'Fail' in Drawing")
if(Computer==50):
    print("You got 'A' grade in Computer")
elif(50>=Computer>=40):
    print("You got 'B' in Computer")
elif(40>=Computer>=30):
        print("You got 'C' grade in Computer")
elif(30>=Computer>=20):
        print("You got 'D' grade in Computer")
elif(20>=Computer>=10):
        print("You are Fail in Computer")
elif(Computer>50):
        print("Invalid marks are entered in Computer")
elif(10>=Computer>-1):
        print("You are Fail in Computer")
        #finally finish
