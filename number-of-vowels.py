if __name__ == '__main__':
    string = input("Enter a string: ")
    count = 0
    for value in string:
        if (value == 'a') or (value =='e') or (value =='i') or (value =='o' ) or (value =='u') :
            count = count + 1
    print(f"Number of vowels = {count}")