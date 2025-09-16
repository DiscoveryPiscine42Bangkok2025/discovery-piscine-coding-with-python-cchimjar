print("Enter the first number: ")
P = int(input())
print("Enter the second number: ")
y = int(input())

multi = P * y
print(f"{P} x {y} = {multi}")

if multi < 0:
    print("The result is negative.")
elif multi > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")