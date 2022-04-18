from collections import Counter

# initializing string
test_str = "aabbbccde"

# using collections.Counter() to get
# count of each element in string
res = Counter(test_str)
# valuesList = list(res.values())
# # printing result
# str1 = str(res)
print(res)
keysList = list(res.keys())
print(keysList)
# print(valuesList)
for item in sorted(res):
    print("{} {}".format(item,res[item]))

