def gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g,x,y
    
a=int(input())
b=int(input())

print(gcd(a,b))
