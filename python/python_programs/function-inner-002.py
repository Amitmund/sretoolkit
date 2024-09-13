def fun1():
    print('Reached fun1')
    
    # creating inner function
    def fun2():
        print('Reached inner function.')
    
    # This will pring first, then the fun2() data will print.
    # as we are calling the inner function at the end of the fun1 first.
    print('Reached outer function now.')
    
    # Calling fun2 in first function.
    fun2()

fun1()

# you can't call fun2 directly.
# you will get 'NameError' if you directly call fun2()
# If you want to design a function not to be called directly,
# you can design that as inner function and call that innter function from
# the parent function. 
# You can uncomment the following line to test it.
# fun2()

print(type(fun1))
# output: <class 'function'>