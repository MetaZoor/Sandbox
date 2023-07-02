# Python function that takes two numbers as arguments and divide the first number by the second. Your function should handle the potential ZeroDivisionError exception.

def checker(a,b):
    try:
        c = a / b
        print("The result is:", c)
    except ZeroDivisionError:
        print("Cannot divide by zero!")

a= 1
b= 2

checker (a,b)

# Python script that writes the numbers from 1 to 10 to a file, and then reads the file and prints the numbers.

# Write to a file
with open('numbers_test.txt', 'w') as f:
    numbers = range(1,11)
    for num in numbers:
        f.write(str(num) + ' ')
    
# Read from a file
with open('numbers_test.txt', 'r') as f:
    print(f.read())


# Python class named Rectangle that is defined by its length and width and a method which will compute the area of a rectangle. Create an object of this class and use this method.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(area)

test_recetangle=Rectangle(5,3)
test_recetangle.area()
