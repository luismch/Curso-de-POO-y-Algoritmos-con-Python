# ley de la suma


def f(n):
    for i in range(n):
        print(i)


    for i in range(n * n):
        print(i)

# 0(n) + 0(n * n) = 0(n + n²) = 0(n²)



# ley de la multiplicacion

def f(n):
    
    for i in range(n):

        for j in range(n):
            print(i, j)

# 0(n) * 0(n) = 0(n * n) = 0(n²)



# recursividad multiple 

def fibonacci(n):
     if n == 0 or n == 1:
         return 1
    
    return fibonacci(n -1) + fibonacci(n - 2)

# 0(2**n)