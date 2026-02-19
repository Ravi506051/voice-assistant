list = [10,3.3,'a',"hello"]
for i in list:
    print(i)
    print(list[0])
    print(list[0:3])
    print(list[2:-1])
    print(list*3)

    #modify

    l = [1,2,3,4,5,6]
    l[1] = 1.5
    print(l)

    l.append(3)
    print(l)

 #tuple   

    tpl = (1,5,7,3)
    print(tpl)
    print(len(tpl))
    print(sum(tpl))
    print(max(tpl))
    print(sorted(tpl))
    print(min(tpl))
    
# range 
r = range(10)
for j in r:
    print(j)
    print(1,2)


#sets

set = {1,2,3,4,5} 
print(set)

set.add(99)
print(set)
print(sum(set))


print("how are you", end='\t')
print("how  ", end='\n')
print("are  ", end='\n')
print("you ", end='\n')

# control sttement
str = 'yes'
if str =='yes':
    print("true")
else:
    print("false")    


x = int(input("Enter a number :"))
if x%2==0:
    print(" Even number ")  
else:
    print("odd number")     


y = int(input("Enter a number :"))
if 1<y<10:
    print("the number between 1 to 10")
else:
    print("not found ")    


z =float(input("Enter a number :"))
if z==0:
    print("number is zero ")
elif z>0:
    print("number is positive ")
else:
    print("number is negative ")            
         
#while
p = 1
while x<=10:
    print(p)
    x+=1
    print("end")



#even num bt 100 to 200
x1 = 100
while   x1>=100 and x1<=200:
    print(x1)
    x1=x1+2


#for loop
str = "how are you "
for ch in str:
    print(ch)

    

r1 = range(1,10,2)
for i1 in r1:
    print(i1)


#function

def sum(a1,b1):
    print("sum is :", a1+b1)
sum(2,4)
sum(1,3)    


#prime no find

max = int(input("Enter the number upto :"))
print(max)
for num in range(2,max+1):
    for i4 in range(2,num):
        if num%i4==0:
            break
    else:
        print(num)


        


