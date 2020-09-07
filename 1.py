# Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. 
# You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100
original_list = [0,1]
number = int(input("Enter a number: "))
for i in range(2,10000):
    fibonacci = original_list[i-1] + original_list[i-2]
    original_list.append(fibonacci)

if number in original_list:
    print("yes")
else:
    print("No")