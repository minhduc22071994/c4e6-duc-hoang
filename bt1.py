from turtle import*
speed(10)
shape("turtle")
for n in range(12,2,-1):
    if n%2 == 0:
        color("green", "yellow")
        print(n)
        begin_fill()
        for _ in range(n):
            forward(100)
            left(180-180*(n-2)/n)
        end_fill()
    else:
        color("red", "purple")
        print(n)
        begin_fill()
        for _ in range(n):
            forward(100)
            left(180-180*(n-2)/n)
        end_fill()
        
