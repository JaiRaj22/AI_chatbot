def emi(amount, rate, time):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if rate <= 0:
        raise ValueError("rate must be positive")
    if time <=0:
        raise ValueError("time duration must be positive")
    
    monthly_rate = rate / 100 / 12
    emi = (amount * monthly_rate * (1 + monthly_rate) ** time) / ((1 + monthly_rate) ** time - 1)
    
    return emi

amount = float(input("enter price ")) 
rate = float(input("enter rate of interest ")) 
time = float(input("enter duration in months "))

try:
    calc = emi(amount, rate, time)
    print(f"monthly emi is {calc}")
except ValueError as e:
     print("error",e)
    