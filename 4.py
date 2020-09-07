#Using reduce function: PTS:100

#add only even numbers in a list
import random 
inp =  random.sample(range(1,100),10)
def sum_even(li):
    sum = 0
    for i in inp:
        if i%2 == 0:
            sum = sum + i
    return sum 
sum_even(inp)

#adds every 3rd number in a list
import random 
inp =  random.sample(range(1,100),10)
sum = 0
for i in range(0, len(inp), 3):
    sum = sum + inp[i]
print(sum)
