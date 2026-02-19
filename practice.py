import statistics

li = [1,2,3,4,5,6,5,6,6,7,7,2,4]
print("the avg of list is ",end="")
print(statistics.mean(li))

print("the mode of list ",end="")
print(statistics.mode(li))

print("the median of list ",end="")
print(statistics.median(li))

print("the variance of list ",end="")
print(statistics.variance(li))

print("the mode of list ",end="")
print(statistics.stdev(li))
