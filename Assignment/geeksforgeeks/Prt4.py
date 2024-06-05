# Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where, P is the principal
# amount T is the time and R is the rate
'''
Input : P = 10000
        R = 5
        T = 5
Output :2500.0
'''


def sim(p, t, r):
    smit = (p*t*r)/100

    return smit

print(sim(10000, 5, 5))


'''
A = P(1 + R/100) t 
Compound Interest = A – P 

Where, 
A is amount 
P is the principal amount 
R is the rate and 
T is the time span
Find Compound Interest with Python
'''

def cmp(p, r, t):
    a = p * (pow((1+r/100), t))
    cm = a-p

    return cm

print(cmp(10000, 10.25, 5))


ls = [1, 2, 3 ,4 ,5]

print(ls.pop(1))
print(ls)
