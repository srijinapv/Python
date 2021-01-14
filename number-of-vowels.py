if __name__ == '__main__':
    string = input("Enter a string: ")
    length_string = len(string)
    count = 0
    for value in range(0,length_string):
        if (string[value] == 'a') or (string[value] =='e') or (string[value] =='i') or (string[value] =='o' ) or (string[value] =='u') :
            count = count + 1
    print(f"Number of vowels = {count}")