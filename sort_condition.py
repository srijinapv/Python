"""
Sort the string in the following manner
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""
import string
S = input()

list1 = [i for i in S]
list1.sort()

small = string.ascii_lowercase
upper = string.ascii_uppercase
digits =string.digits

listsmall = [j for j in list1 if j in small]
listupper = [k for k in list1 if k in upper]
numbers = [int(p) for p in list1 if p in digits]
odd = [str(q)for q in numbers if q%2 !=0]
even = [str(r)for r in numbers if r%2 == 0]

newlist = listsmall + listupper+ odd+even
result = ''.join(newlist)

print(result)
