def add(x,*y):
    print(x)
    print(y)
    c=x
    for i in y:
        c=c+i
    print(c)


add(4,5,4,66)
