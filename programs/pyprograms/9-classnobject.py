print("Class")
print("Create calculator class")
class Calculator():
    def add(self,num1,num2):
        return num1+num2    
    def subtract(self,num1,num2):
        return num1-num2
    def multiply(self,num1,num2):
        return num1*num2
print("object and its methods")
mycalculator1=Calculator()
result =mycalculator1.add(10,15)
print("result of addition is ",result)
result =mycalculator1.subtract(10,15)
print("result of subtraction is ",result)
result =mycalculator1.multiply(10,15)
print("result of multiplication is ",result)


    
