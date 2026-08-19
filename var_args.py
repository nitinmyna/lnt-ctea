def my_function1(arg1, arg2):
    pass
# This function exactly takes 2 arguments of any time.

def my_function2(arg1: float, arg2: str) -> str:
    pass
    # Say suppose we pass some other type of data, this may not work.

def my_function1(arg1='mysuru', arg2=10):
    pass
# This function works even if it is called 0 or 1 argument. 2 as well. Thats the advantage we get by using the default args.

def another_function():
    pass

def another_function(arg1, arg2=50):
    pass

def another_function(arg1 = 'default1', arg2='default2'):
    pass

# Here since we have 3 funcstions with same name. Hence only the last function definition will be stored and the 1st 2 will be not.

another_function()
another_function('string1')
another_function('string1', 'string2')
another_function(arg2='string1', arg1='string2')

def another_function(*args):
    pass

another_function()
another_function('string1')
another_function('string1', 'string2')
another_function(arg2='string1', arg1='string2')

'''
All of the above calls can happen alone to the last definition (Line #28)
# Here args is a tuple. It can consist of 0 to many args in it.

'''
