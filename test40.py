class Date:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y, '/', self.m, '/', self.d)\

    def GetMonthName(self):
        if self.m == 1:
            print('Farvardin')
        if self.m == 2:
            print('Ordibehesht')
        if self.m == 3:
            print('Khordad')
        if self.m == 4:
            print('Tir')
        if self.m == 5:
            print('Mordad')
        if self.m == 6:
            print('Shahrivar')
        if self.m == 7:
            print('Mehr')
        if self.m == 8:
            print('Aban')
        if self.m == 9:
            print('Azar')
        if self.m == 10:
            print('Dey')
        if self.m == 11:
            print('Bahman')
        if self.m == 12:
            print('Esfand')

    def IsValidDate(self):
        if self.d < 1 or self.d > 30:
            print('False')
        else:
            print('True day')
        if self.m < 1 or self.m > 12:
            print('False')
        else:
            print('True month')
        if self.y < 1 or self.y > 9999:
            print('False')
        else:
            print('True year')
        
date1 = Date(1401, 11, 24)
date1.show()
date1.GetMonthName()
date1.IsValidDate()