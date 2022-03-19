"""def f1():
    print("F1")

f2 = f1
del f1
f2()
"""

"""def fun(num):
    if num == 0:
        return print
    elif num == 1:
        return sum


a = fun(1)
print(a)
"""


def dec1(func1):
    def nowexc():
        print("Executing now")
        func1()
        print("Ececuted")
    return nowexc

@dec1
def who_is_harry():
    print("Harry is a good Boy")


#who_is_harry = dec1(who_is_harry)
who_is_harry()
