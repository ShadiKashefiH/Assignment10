class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def show(self):
        print(self.h, ':', self.m, ':', self.s)

    def sum(self, t):
        result = Time(None, None, None)
        result.h = self.h + t.h
        result.m = self.m + t.m
        result.s = self.s + t.s

        if result.s >= 60:
            result.s -= 60
            result.m += 1

        if result.m >= 60:
            result.m -= 60
            result.h += 1
        
        return result

    def sub(self, t):
        result = Time(None, None, None)
        if self.h > t.h:
            result.h = self.h - t.h
            result.m = self.m - t.m
            result.s = self.s - t.s
        else:
            result.h = t.h - self.h
            result.m = t.m - self.m
            self.s = t.s - self.s

        if result.s < 0:
            result.m -= 1
            result.s += 60

        if result.m < 0:
            result.h -= 1
            result.m += 60
            
        return result

    def TimeToSeconds(self):
        result = self.s + self.m*60 + self.h*3600
        print(result)
    
    def SecondsToTime():
        result = Time(None, None, None)
        result.h = s // 3600
        result.m = (s%3600) // 60
        result.s = (s%3600) % 60
        return result
        
time1 = Time(10, 20, 25)
time1.show()

time2 = Time(8, 30, 40)
time2.show()

result_sum = time1.sum(time2)
result_sum.show()

result_sub = time1.sub(time2)
result_sub.show()

time3 = Time(8, 50, 21)
time3.TimeToSeconds()

s = input('Seconds:')
result_SecondsToTime = SecondsToTime()
result_SecondsToTime.show()