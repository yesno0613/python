def root_ex(a,b,c):
    x_1 = (-b +(b**2 -4*c)**0.5)/(2*a)
    x_2 = (-b +(b**2 -4*c)**0.5)/(2*a)

    return x_1 , x_2

a = int(input('이차함수계수'))
b = int(input('일차함수계수'))
c = int(input('상수형'))

x = root_ex(a,b,c)
print(x)
