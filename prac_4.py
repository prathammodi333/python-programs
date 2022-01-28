# Name : PRATHAM MODI
# ID : 20CE056
# Aim :  Find runner-up from given list
# GITHUB LINK : https://github.com/prathammodi333/python-programs
list1 = []
  
# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))
  
# iterating till num to append elements in list
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)
set1 = set(list1)
set1.remove(max(set1))
print(max(set1))
