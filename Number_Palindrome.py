"""
Check number is palindrome or not, if not add reverse of that number and continue the steps till number becomes palindrome
"""

def palindrome(num):
    count = 0
    while True:
        str_num = str(num)
        rev_num = str_num[::-1]
        if str_num == rev_num:
            return num,count
            break
        else:
            num = num + int(rev_num)
            count = count+1
        if count > 30 :
            return ("Palindrome is not possible")
            break

if __name__ == '__main__':
    num = int(input("Enter a number :- "))
    print(palindrome(num))