import random
import itertools
lst1 = []
lst2 = []
for i in range(0,10):
    n1 = random.randint(0,20)
    n2 = random.randint(0,20)
    lst1.append(n1)
    lst2.append(n2)
print(lst1)
print(lst2)
# for j,k in itertools.zip_longest(lst1,lst2):
#     if j == k:
#         print(j)
print(list(set(lst1).intersection(set(lst2))))