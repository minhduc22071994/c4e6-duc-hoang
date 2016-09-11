while True:
    x=int(input("What is your height(cm)? "))
    print(x)
    y=int(input("What is your weight(kg)? "))
    print(y)
    t=(x/100)*(x/100)
    z=y/t
    print("Your BMT(Body Mass Index)")
    print(z)
    if z < 16 :
        print("Severely underweight (còi xương)")
    elif 16<z<18.5:
        print("Underweight (Thiếu cân)")
    elif 18.5<z<25:
        print("Normal (Bình thường)")
    elif 25<z<30:
        print("Overweight (Thừa cân)")
    else:
        print("Obese (Béo phì)")
    
