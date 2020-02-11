def x(n, m):
    print('-')
    if n == m or m == 0:
        return 1
    else:
        return x(n-1,m) + x(n-1,m+1)

#print(x(5,3))

def y(n):
    print('-')
    if n >= 0 and n <= 2:
        return n
    else:
        return y(n-1) + y(n-2) + y(n-3)

#print(y(6))

def z(n):
    if n == 0:
        print(n)
    else:
        #<espaço B>
        z(n-1)
        print(n)
        #<espaço C>
    #<espaço D>
#<espaço E>

print(z(10))