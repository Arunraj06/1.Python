class MultipleFunction():
    def sub_fields():
        print("Sub-fields in AI are:")
        AI=["Machine Learning","Neural Networks","Vision","Robotics","Speech                 Processing","Natural Language Processing"]
        for fields in AI:
            print(fields)
    
    def Oddeven():
        num =int(input("Enter a number:"))
        if(num%2==0):
            print("Even number")
            num_type="The given number is even"
        else:
            print("Odd number")
            num_type="The given number is odd"
            return num_type
            
       
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if (age>=18):
            print ("Your are eligible for marriage")
        else:
            print("your are not eligible for marriage")
    def Percentage():
        Subject1=int(input("Tamil=")) 
        Subject2=int(input("English=")) 
        Subject3= int(input("Mathes=")) 
        Subject4= int(input("Science=")) 
        Subject5= int(input("Social science="))
        Total =Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",Total)
        Percentage=float(Total/5)
        print("Percentage:",Percentage)
    def triangle():
        #Area of triangle
        print("Area of triangle==>")
        Height=int(input("Height:"))
        Breadth=int(input("breadth:"))
        print("Area of triangle:",(Height*Breadth)/2)
        #Perimeter of triangle
        print("Perimeter of triangle==>")
        Height1=int(input("Height1:"))
        Height2= int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter of Triangle:",Height1+Height2+Breadth)