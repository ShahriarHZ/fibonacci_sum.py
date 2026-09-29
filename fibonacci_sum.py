# Sum of Fibonacci Series

n = int(input("Enter number of terms: "))

a = 0
b = 1
sum = 0

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    sum = sum + a

    c = a + b
    a = b
    b = c

print()
print("Sum =", sum)
