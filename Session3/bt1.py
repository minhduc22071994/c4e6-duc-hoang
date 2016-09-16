color_list = ['Blue','Red','Black','Pilk', 'Brown', 'Yellow']
print('My color list')
print(color_list)
print('Color_list at index 3:', color_list[3])
while True:
    x = input('Enter a number from 0-5:')
    print("Your color: ", color_list[int(x)])
    print(color_list)
    for color in color_list:
        print(color)
    y = input("What is your favorite color?")
    found = False
    for i in range(len(color_list)):
        if y == color_list[i]:
            print('Your color is at index {0} in my list.'.fomat (i))
            found = True
        if found == False:
            print("Sorry, I could not find your color.")
