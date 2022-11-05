class Assignment:
    def __init__(self, days):
        self.days = days
        self.ways_to_attend = self.ways_to_attend_classes()

    def no_ways_attend_classes(self):
        return len(self.ways_to_attend)

    def probability_to_miss_ceremony(self):
        filter_ways = self.filter_out_four_consicutive()
        return len(filter_ways) / self.no_ways_attend_classes()

    def ways_to_attend_classes(self):
        arr=[]
        attendance = ""
        self.rec(self.days, attendance, arr)
        return arr

    def rec(self, days, attendance, arr):
        if days == 0:
            arr.append(attendance)
        else:

            self.rec(days - 1, attendance + 'A', arr)
            self.rec(days - 1, attendance + 'P', arr)

    def filter_out_four_consicutive(self):
        return list(filter(lambda way: "AAAA" in way, self.ways_to_attend))

