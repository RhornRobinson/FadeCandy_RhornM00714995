value = input('''Welcome to the menu. Options are listed below:,
              \t 1.Roll
              \t 2. Sweep
              \t 3. Scroll
              Type the number of your choice and press Enter.''') #\n - newline; \t - tab

#print("The value you input is:", value)
#print(f'it is of type {type(value)}.')

def func1(val):
    return val**val
def func2(val):
    return val**val
def func3(val):
    return val**val

while True:
    if value.isdigit() == True: # .isdigit() 
        value = int(value)
        if value >3 or value <1 : #if the value is outside our parameters
             value = input ("Please input a number between 1 and 3. ")
             continue # skip the rest of the loop, start from isdigit() check again
        else:
            break # on correct value datatype: exit the loop
    else:
        value=input("invalid input, please provide an integer:") #ask for a new value
#print("The converted is:", value)
#print(f'it is of type {type(value)}.')

#compare numeric value to choices available, perform assicoated function or sequence.
if value == 1:
    print(func1(value))
    for x in range(0, value):
            
            led[308] = (0,0,220);     led[328] = (0,0,220);
            led[308] = (0,0,220);     led[328] = (0,0,220);
            led[308] = (0,0,220);     led[328] = (0,0,220);
            led[308] = (0,0,220);     led[328] = (0,0,220);
            led[308] = (0,0,220);     led[328] = (0,0,220);
elif value == 2:
    print(func2(value))
elif value == 3:
    print(func3(value))

    
            
            
