def fib(n):
   if n == 0:
       return 0
   elif n == 1:
       return 1
   else:
       return fib(n - 1) + fib(n - 2)

n = int(input("Hasta que valor quiere Fibonacci? "))
b=2
while b < n:
    c = fib(b)
    if c<n:
        print(c)
        b=b+1
    else:
        break

print("Gracias");
