number = int(input("Take a number to reverse : "))

reverse = 0

while number != 0:
    digit = number % 10
    reverse = reverse*10 + digit
    number//=10

print("Reversed number is : ",reverse)