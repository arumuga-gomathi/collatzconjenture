#This program is designed to classify numbers as even or odd. A simple implementation of the Collatz Conjecture
def check_number(num):
    if num % 2 == 0:
        result = num // 2
    else:
        result = num * 3 + 1
    return result

num = int(input("enter an integer:"))
result = check_number(num)
print("Result: ",result)