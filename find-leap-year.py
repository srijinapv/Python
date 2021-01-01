class Year:
    def __init__(self,year):
        self.year = year


    def leap(self):

        if self.year % 4 != 0 and self.year % 400 != 0:
            leap_y = False
        else:
            leap_y = True
        if self.year in [1800, 1900, 2100, 2200, 2300, 2500]:
            leap_y = False
        return leap_y



if __name__ == '__main__':
    year_choice = int(input('year : '))
    year_obj = Year(year_choice)
    print(year_obj.leap())


