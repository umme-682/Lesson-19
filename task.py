# program to find multiple with 1 and N iterations

# for 1 iterations simply multipy 
def o1(n, m):
    total = n * m
    print("\n1 iteration : 1")
    
# for N iteration run a for loop
def oN(n, m):
    total = 0
    for i in range(1, n+1):
        total += m
    print("N iteration: ", n)
          
m = int(input("Enter 'a' for a*b: "))
n = int(input("Enter 'b' for a*b: "))

o1(m, n)
oN(m, n)