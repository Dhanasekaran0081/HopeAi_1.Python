class SubfieldsInAI():

    # Create a class and function, and list out the items in the list
    def Subfields():
        sf = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for field in sf:
            print(field)

class OddEven():

    # Create a function that checks whether the given number is Odd or Even
    def OddEven():
        num = int(input("Enter the number:"))
        if((num%2)==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")

class ElegiblityForMarriage():

    # Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
    def Elegible():
        
        gender = input("Your Gender:")
        age = int(input("Your age:"))
        
        if gender.lower() =="male":
            if age >= 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        if gender.lower() =="female":
            if age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")

class FindPercent():

    # calculate the percentage of your 10th mark
    def percentage():
    
        Subject1 = 98
        Subject2 = 87
        Subject3 = 95
        Subject4 = 95
        Subject5 = 93
    
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
    
        Percentage = (Total / 500) * 100
    
        print("Subject1=", Subject1)
        print("Subject2=", Subject2)
        print("Subject3=", Subject3)
        print("Subject4=", Subject4)
        print("Subject5=", Subject5)
        print("Total  :", Total)
        print("Percentage : ", Percentage)

class triangle():

    #print area and perimeter of triangle using class and functions
    def triangle():
        
        height = 32
        breadth_a = 34
    
        area = (height*breadth_a)/2
    
        height1 = 2
        height2 = 4
        breadth_p = 4
    
        perimeter = height1 + height2 + breadth_p
    
        print("Height:",height)
        print("Breadth:",breadth_a)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",area)
        print("Height1:",height1)
        print("Height2:",height2)
        print("Breadth:",breadth_p)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",perimeter)