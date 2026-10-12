print("Simple interest with user inputs")
p=input("Enter principal ")
r=input("Enter rate of interest")
t=input("Enter time in years")
#si=(p*r*t)/100
print("data type of p ",type(p))
print("typecasting ")
si=(int(p)*int(r)*int(t))/100
print("simple interest is ",si)

"""
Assignment - SimpleCalculator with user inputs
inputs - ask user to enter two number and operation(+,-,*,/)
based on the operation call different methods such as
add(num1,num2)
sub(num1,num2)....
"""
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
operator = input("enter +,-,*,/")
num1=int(input("Enter first number")
num2=int(input("Enter second number")
result=0
if(operator=="+"):
         result = add(num1,num2)
elif(operator=="-"):
         result = sub(num1,num2)
print(num1," ",operator, " ",result)




