class Theory:
    def __init__(self,t1marks,t2marks):
        self.t1marks = t1marks
        self.t2marks = t2marks

class Practical:
    def __init__(self,p1marks,p2marks):
        self.p1marks = p1marks
        self.p2marks = p2marks

class TotalMarks(Theory,Practical):
    def __init__(self, t1marks,t2marks,p1marks,p2marks):
        Theory.__init__(self, t1marks,t2marks)
        Practical.__init__(self, p1marks,p2marks)

    def total(self):
        total = self.t1marks + self.t2marks + self.p1marks + self.p2marks
        return total

    def percentage(self):
        percentage = (obj.total() * 100 ) /400
        return percentage
if __name__ == '__main__':
    t1marks = int(input("Theory mark1:"))
    t2marks = int(input("Theory mark2:"))
    p1marks = int(input("Practical mark1:"))
    p2marks = int(input("Practical mark2:"))

    obj = TotalMarks(t1marks,t2marks,p1marks,p2marks)
    print(f"Total mark is {obj.total()}")
    print(f"Percentage mark is {obj.percentage()}")