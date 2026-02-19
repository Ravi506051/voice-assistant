#sum of two num
def sum(a,b):
    c =a+b
    return c
x =sum(10,9)
print("the sum is ",x)


#even odd

def even_odd(num):
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
even_odd(12)
even_odd(10)         


#sum sub
def sum_sub_mul_dev(p,q):
    a1 = p+q
    a2 = p-q
    a3 = p*q
    a4 = p/q
    return a1,a2,a3,a4
t = sum_sub_mul_dev(10,5)
print('the result are')
for i in t:
    print(i)


#funinfun
def display():
    def message():
        return 'how are you'
    return message
fun = display()
print(fun())    


#dir
