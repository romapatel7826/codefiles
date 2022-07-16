sub1 = int(input("enter your first sub marks: "))
sub2 = int(input("enter your second sub marks: "))
sub3 = int(input("enter your third sub marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("your are fail because your marks is less then 33 in each subject")

elif(sub2+sub2+sub3)/3 < 40:
    print("your are fail becuaee your percentage is less thenn 40 perce")

else:
    print("congrs your are pass")