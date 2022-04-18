from itertools import combinations
#The first line of input will contain space-separated integers.
values =[int(i) for i in input('Enter space-separated integers: ').split()]
values.sort()
#The second line of input will contain an integer, denoting K.
K = int(input('Enter K: '))
#The output should be containing the count of all unique combinations of numbers whose sum is equal to K
counterUniqueCombinations=0

for i in range(1, len(values)+1):
    com =list(set(combinations(values, i)))
    for combination in com:
        if sum(combination) == K:
            counterUniqueCombinations += 1
print(f"The count of all unique combinations is: {counterUniqueCombinations}")