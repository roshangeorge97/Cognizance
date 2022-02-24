num=int((input("Number:")))
# storing value of input in a variable number
number=num
reverse_num=0
while(num>0):
    rem=num%10
    reverse_num=reverse_num*10+rem
    num=num//10
# comparing input and reverse number obtained
if (reverse_num==number):
 print("True")
else:
 print("False")
