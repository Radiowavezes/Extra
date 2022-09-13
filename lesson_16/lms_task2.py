class Mathematician:
    def square_nums(self, input_list):
        return [item**2 for item in input_list]

    def remove_positives(self, input_list):
        return [item for item in input_list if item < 0]

    def filter_leaps(self, input_list):
        def leap(year):
            if year % 400 == 0 and year % 100 == 0:
                return year
            elif year % 4 == 0 and year % 100 != 0:
                return year
            else:
                return False    
        return list(filter(leap, input_list))


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
