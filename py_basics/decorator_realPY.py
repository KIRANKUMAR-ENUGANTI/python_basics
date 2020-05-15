import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"



make_greeting("Benjamin")
make_greeting("Richard", age=112)
make_greeting(name="Dorrisile", age=116)



print('\n\n\n♥♥')
def secret(fun):
    pass
@secret
def normal():
    print('im always normal')

try:
   normal()
except:
    print('raised exception')




print('\n\n\n♥♥')
def secret2(fun):
    return fun


@secret
def normal2():
    print('im always normal')


try:
    normal2()
except:
    print('raised exception')




print('\n\n\n♥♥♥')
def secret3(fun):
    def inner_fun(*args,**kwargs):
        print('has been decoratored')
        k=fun(*args,**kwargs)
        return k
    return inner_fun
@secret3
def add(a,b):
    return a+b
print(add(1,2))