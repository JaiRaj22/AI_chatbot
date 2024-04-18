import math
class Operations:
    def __init__(self):
        pass
    def prime(self, n):
        if n == 0 or n == 1:
             return n
        flag = False
        for i in range(2,n):
            if n % i == 0:
                flag = True
                break
        if flag:
            print("not prime")
        else:
            print("prime")
            
    def factorial(self, n):
        if n == 0 or n == 1:
            return n
        fact = 1
        for i in range(1, n+1):
            fact = i * fact
        return fact
    
    def permutation(self, n,r):
        if n == 0 or n == 1:
            return n
        print(math.perm(n,r))
    
    def combination(self, n,r):
        if n == 0 or n == 1:
            return n
        print(math.comb(n,r))
    
    def fibionacci(self, f):
        n1 = 0
        n2 = 1
        fibio = []
        for i in range(2,f):
            n3 = n2 + n1
            n1 = n2
            n2 = n3
            fibio.append(n3)
        print(fibio)
        
ops = Operations()
ops.prime(56)
print(ops.factorial(5))
ops.permutation(5,2)
ops.combination(5,2)
ops.fibionacci(5)
            
        