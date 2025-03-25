
from datetime import datetime
months = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class time_format:
    def __init__(self, time_format):
        self.year = time_format[0]
        self.month = time_format[1]
        self.day = time_format[2]
        self.hour = time_format[3]
        self.minute = time_format[4]
        self.second = time_format[5]
        self.time_transformation()

    def time_transformation(self):
        self.total_year_days = 365
        self.total_month_days = months[self.month]
        if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
            self.total_year_days += 1
            if self.month == 2:
                self.total_month_days += 1
        
        self.year_days = sum(months[1:self.month]) + self.day - 1
        if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
            if self.month > 2:
                self.year_days += 1

        self.month_days = self.day - 1
        self.seconds = self.hour * 3600 + self.minute * 60 + self.second

    def compare(self, target, method):
        # target -> self (timeline)
        year_diff = self.year - target.year
        month_diff = self.month - target.month
        if method == 'Year':
            E = (self.year_days * 86400 + self.seconds) * (target.total_year_days * 86400) 
            S = (target.year_days * 86400 + target.seconds) * (self.total_year_days * 86400)

            return year_diff - (E < S)
        elif method == 'Month':
            E = (self.month_days * 86400 + self.seconds) * (target.total_month_days * 86400) 
            S = (target.month_days * 86400 + target.seconds) * (self.total_month_days * 86400)

            return year_diff * 12 + month_diff - (E < S)
        elif method == 'Day':
            bias = 0
            if self.year > 5000:
                mod = (self.year - 5000) // 400
                bias += (365 * 400 + 100 - 4 + 1) * mod
                self.year -= mod * 400
            if target.year > 4000:
                mod = (target.year - 4000) // 400
                bias -= (365 * 400 + 100 - 4 + 1) * mod
                target.year -= mod * 400

            E = datetime(year=self.year, month=self.month, day=self.day)
            S = datetime(year=target.year, month=target.month, day=target.day)

            return (E - S).days - (self.seconds < target.seconds) + bias
        else:
            return None

ANS = []
for _ in range(int(input())):
    S = list(map(int, input().split()))
    E = list(map(int, input().split()))
    C = input()

    PS = time_format(S)
    PE = time_format(E)
    ANS.append(PE.compare(PS, C))

print(*ANS, sep='\n')