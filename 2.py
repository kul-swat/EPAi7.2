#Using list comprehension (and zip/lambda/etc if required) write an expression that:

#add 2 iterables a and b such that a is even and b is odd
import random 
l1 =  random.sample(range(1,100),10)
l2 =  random.sample(range(1,100),10)
list =[]
for i in range(len(l1)):
    if l1[i]%2 == 0:
        if l2[i]%2 != 0:
            sum = l1[i] + l2[i]
            list.append(sum)
print(list)

#strips every vowel from a string provided (tsai>>t s)
input_str = input()
vowel = ["a","e","i","o","u"]
output = []
for i in input_str:
    if i not in vowel:
        output.append(i)
print(' '.join(map(str, output)))

#acts like a ReLU function for a 1D array
import random 
inp =  random.sample(range(-50, 50),10)
op=[]
for i in inp:
    if i > 0:
        op.append(i)
    else:
        i = 0
        op.append(i)
print(op)

#acts like a sigmoid function for a 1D array
import random 
inp =  random.sample(range(-50, 50),10)
op=[]
for i in inp:
    if i > 0:
        op.append(1)
    elif i==0:
        op.append(0)
    else:
        op.append(-1)
print(op)

#
        