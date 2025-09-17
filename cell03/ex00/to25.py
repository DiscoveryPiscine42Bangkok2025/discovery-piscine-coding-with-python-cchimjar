print("Enter a number less than 25")
x = int(input())

if x >= 25:
    print("Error")
else:
    for i in range(x , 26):
        print(f"Inside the loop, my variable is {i}")