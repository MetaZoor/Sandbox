a = 1
b = 3
c = 5

## Determining the biggest number with If-Elif-Else conditions

## This approach is not counting the condition that a or b or c could be equal to each other so it will generate errors. I will commented it out for learning purposes 
## if a > b and a > c:
##    print ("A is the biggest number")
## elif b > a and b > c:
##    print ("B is the biggest number")
## else:
##    print ("C is the biggest number")

if a > b and a > c:
    print("A is the biggest number")
elif b > a and b > c:
    print("B is the biggest number")
elif c > a and c > b:
    print("C is the biggest number")
elif a == b and a > c:
    print("A and B are the biggest numbers, and they are equal to each other")
elif a == c and a > b:
    print("A and C are the biggest numbers, and they are equal to each other")
elif b == c and b > a:
    print("B and C are the biggest numbers, and they are equal to each other")
else:
    print("There are numbers that are equal to each other")

# Iterating over a list from 1 to 10 in a sequential order
for x in range(1, 11):
    print(x)

## This is an  symplified approach so commenting it as I want to automate the process more
# Iterating over a list from 1 to 10 in non sequential order
##for x in [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]:
##    print(x)

# Printing numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1