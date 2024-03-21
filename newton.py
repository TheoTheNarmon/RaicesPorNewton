def f(x):
    return (x**2)-2

def fPrima(x):
    return 2*x

x = 2
xx = 0
epsilon = 0.1

xx = x
x = x - (f(x)/fPrima(x))

while(abs(xx-x) > epsilon):
    xx = x
    x = x - (f(x)/fPrima(x))
    
print(x)
print(f(x))