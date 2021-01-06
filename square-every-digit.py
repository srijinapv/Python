class SquareDigit:

    def __init__(self,number):
        self.number = number

    def square(self):
        strnumber = str(self.number)
        result = ''
        for value in range(0, len(strnumber)):
            square_digit = int(strnumber[value]) * int(strnumber[value])
            result = result + str(square_digit)
        return result

if __name__ == '__main__':
    number = int(input("Enter the number : "))
    number_obj = SquareDigit(number)
    print(number_obj.square())


