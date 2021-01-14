if __name__ == '__main__':
    number = int(input("Enter number to be reversed:"))
    str_number = str(number)
    length_number = len(str_number)
    reverse_number = []
    for value in range(1,length_number+1):
        new_value = str_number[-value]
        #new_valueeeeee = int(new_value)
        result = reverse_number.append(new_value)
    print(''.join(reverse_number))


