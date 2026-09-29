Sum of Fibonacci Series

Problem

Write a Python program to generate the first n Fibonacci numbers and find their sum.

Algorithm

Start.

Take the number of terms n.

Initialize a = 0, b = 1, and sum = 0.

Repeat n times:

Print a.

Add a to sum.

Calculate c = a + b.

Set a = b.

Set b = c.

Print the Fibonacci series.

Print the sum.

Stop.

Example

For n = 7:

Fibonacci Series:
0 1 1 2 3 5 8

Sum = 20

Because:

0 + 1 + 1 + 2 + 3 + 5 + 8 = 20

Time Complexity

O(n) — Linear Time

The loop runs n times.

Python Code

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

Sample Output

Enter number of terms: 7
Fibonacci Series:
0 1 1 2 3 5 8
Sum = 20
