class Age:
    def __init__(self,age):
        self.age = age

    def convert(self):
        days = self.age * 365
        return days


if __name__ == '__main__':
    age = int(input("Enter age : "))
    age_obj = Age(age)
    print(f'Person is {age_obj.convert()} days old')