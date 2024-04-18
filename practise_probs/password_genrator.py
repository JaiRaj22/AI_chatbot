import random
import string

length = 10
password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
result = ''.join(random.choices(password, k=length))
print(result)