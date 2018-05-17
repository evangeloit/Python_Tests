# Loops and Iterations

#break and continue

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found')
        continue # just ignore the value but nor break out of the loop completely
        # break # breaks out of the loop cmpltly and the rest of the nums dont print
    print(num)

# A loop within a loop/Nested loops

for num in nums:
    for letter in 'abc':
        print(num, letter)


# go through loop for a certain number of times

for i in range(1,11): # not including 11
    print(i)

# While loops

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# Infinite loop / you need to break somehow

while True:
    if x == 5:
        break
    print(x)
    x += 1

