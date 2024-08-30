# your function name can't have - in it.

def my_fun():
    print("I am from function")

    # To use return, you need to assign it to a python data type.
    # You can't directly use return in python.
    
    output1 = print("I am from output1 return.")

    output2 = print("I am from output2 return.")
    return(output1, output2)

my_fun()