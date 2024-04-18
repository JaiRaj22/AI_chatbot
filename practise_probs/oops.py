class Triangle:
    def __init__(self):
        pass
    def equilateral(self,a,b,c):
        if a == b == c:
            return True
        else:
            return False
    def scalene(self,a,b,c):
        if a != b != c:
            return True
        else:
            return False
    def isoceles(self,a,b,c):
        if a == b or a == c or b == c:
            return True
        else:
            return False
check = Triangle()
print(check.equilateral(3,3,3))
print(check.scalene(1,1,3))
print(check.isoceles(4,4,1))

