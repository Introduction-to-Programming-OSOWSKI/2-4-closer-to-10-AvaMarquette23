#WRITE YOUR CODE IN THIS FILE
def close10(x,y):
    x=abs(x)
    y=abs(y)
    if x-10<y-10:
        return x
    elif y-10>x-10:
        return y
    else:
        return 0