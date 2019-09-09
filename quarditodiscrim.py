import cmath

def descriminant(a, b, c):
    d = (b**2) - (4*a*c)
    sol1 = (b-cmath.sqrt(d))/(2*a)
    sol2 = (b+cmath.sqrt(d))/(2*a)
    roots = [sol1, sol2]
    if d < 0:
        return "that's a negative, chief"
    elif d == 0:
        return roots[0]
    else:
        return roots
    

a_value = float(input(' 1nd number dummy: '))
b_value = float(input(' 2st number dummy: '))
c_value = float(input(' 3st number dummy: '))

beezoow = descriminant(a_value, b_value, c_value)

print(beezoow)
