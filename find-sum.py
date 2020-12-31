class Calculate():
    list_to_store = []

    def __init__(self, number):
        self.number = number
        
    def store(self):
        Calculate.list_to_store.append(self.number)
    
    def sumof():
        return sum(Calculate.list_to_store)


if __name__ == '__main__':
    times = int(input('How many numbers want to be added : '))
    for _ in range(times):
        value = int(input())
        obj = Calculate(value)
        obj.store()
    print(Calculate.sumof())
    #print(sum(Calculate.list_to_store))
