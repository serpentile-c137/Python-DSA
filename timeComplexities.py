array = [1, 2, 3, 4, 5]

######  Constant time complexity  #######
print('######  Constant time complexity  #######')
print(array[0])


######  Linear time complexity  #######
print('######  Linear time complexity  #######')
for element in array:
     print(element)


######  Logarithmic time complexity  #######
print('######  Logarithmic time complexity  #######')
for index in range(0,len(array),3):
     print(array[index])


######  Quadratic time complexity  #######
print('######  Quadratic time complexity  #######')
for x in array:
    for y in array:
         print(x,y)


######  Exponential time complexity  #######
print('######  Exponential time complexity  #######')
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


######  Add vs Multiply ####### 
arrayA = [1,2,3,4,5,6,7,8,9]
arrayB = [11,12,13,14,15,16,17,18,19] 

for a in arrayA:
    print(a)

for b in arrayB:
    print(b)

for a in arrayA:
    for b in arrayB:
        print(a,b)

######  Iterative algorithm - finding the biggest number in the array ####### 

sample1Array = [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]

def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0]
    for index in range(1,len(sampleArray)):
        if sampleArray[index] > biggestNumber:
            biggestNumber = sampleArray[index]
    print(biggestNumber)

findBiggestNumber(sample1Array)

######  Recursive algorithm - finding the biggest number in the array ####### 

def findMaxNumRec(sampleArray, n):
    if n == 1:
       return sampleArray[0]
    return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1))

print(findMaxNumRec(sample1Array,len(sample1Array)))


######  Recursive algorithm multiple calls ####### 

def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-1)

print(f(3))