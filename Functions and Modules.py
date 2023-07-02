
## Python function that multiplies all the numbers in a list.
def multiply_all(numbers):
    result = 1
    for num in numbers:
        ## The *= operator in Python is a shorthand assignment operator used for multiplication and assignment. It multiplies the value of a variable with another value and assigns the result back to the same variable.
        result *= num
    return result

test = range(1,11)
print(multiply_all(test))


## Python function that checks whether a passed string is palindrome or not (A palindrome is a string that reads the same forwards and backwards).
def palindrome_check(word):
    start = 0
    end = len(word) - 1

    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

test_2 = "apple"
test_3 = "apccpa"

print (palindrome_check(test_2))
print (palindrome_check(test_3))


## Write a Python script that imports the random module and generates a random number between 0 and 10.
import random

random_number = random.choice(range(1, 101))
## randint is nice but I wanted a simpler approach
##random_number = random.randint(1,100)

print (random_number)
