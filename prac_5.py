# Name : PRATHAM MODI
# ID : 20CE056
# Aim :  You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. Sample Input: HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".
# GITHUB LINK : https://github.com/prathammodi333/python-programs
def swap_case(s):
    num = ""
    for let in s:
        if let.isupper() == True:
            num+=(let.lower())
        else:
            num+=(let.upper())
    return num

s = input("Enter the String : ")
print(swap_case(s))