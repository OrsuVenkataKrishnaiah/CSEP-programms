
def compound_interest(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)
p=int(input("Enter the principle :"))
r=float(input("Enter the rate :"))
t=int(input("Enter the time :"))
compound_interest(p, r, t)