# print([n**2 for n in range(10) if n % 2 == 0])

# def gen(n):
#     while True:
#         yield n

# a = gen(8) 

# for i in a:
#     print(i)

# b = (n**2 for n in range(10) if n % 2 == 0)

# for i in b:
#     print(i)

# def wrapper(a):
#     def func2(b):
#         print(a,b)

#         return 
#     return func2

# f = wrapper(1)
# f(2)

# n = 0

# def counter(wrapper):
#     def wrapper():
#         wrapper()
#         global n
#         n += 1
#         print(f'Функция была вызвана {n} раз')
#     return wrapper

# @counter
# def some():
#     print('Hello')

# some()
# some()
# some()
# some()

# print(some.__dict__)

from time import time
# t1 = time() 
# print(time())
def decor(func):  

    def wrapper(n):
        print(wrapper)
        print(wrapper.__dict__)
        if n in wrapper.__dict__:
           
            
            return wrapper.__dict__[n]
        else:
            m = func(n)
            wrapper.__dict__[n] = m
            
            
            return m
    return wrapper

@decor
def square(n):
    return n**2


t1 = time() 
print(square(2000))
t2 = time() 
o = t2 - t1
print(o)
t1 = time() 
print(square(30))
t2 = time() 
o = t2 - t1
print(o)
t1 = time() 
print(square(500000))
t2 = time() 
o = t2 - t1
print(o)
t1 = time() 
print(square(2000))
t2 = time() 
o = t2 - t1
print(o)
print(square.__dict__)