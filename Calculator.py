class StringCalculator:

    def __init__(self,data_entry):
        self.data_entry = data_entry
        self.delimiter = self.get_delimiter()

    def get_delimiter(self):
        return self.data_entry[2:3]

    def add(self):
        sum = 0
        for factor in self.data_entry[4:].replace('\n',self.delimiter).split(self.delimiter):
            sum += int(factor)
        return sum

'''def sum(string_numbers):
    if len(string_numbers) == 0:
        return 0
    elif len(string_numbers) >= 1:
        return sum_uknow_numbers(string_numbers)

def sum_two_numbers(string_numbers):
    sum = 0
    for factor in string_numbers.split(','):
        sum += int(factor)
    return sum

def sum_uknow_numbers(string_numbers):
    sum = 0
    for factor in string_numbers.replace('\n',',').split(','):
        sum += int(factor)
    return sum

def sum_whit_delimiter(string_numbers):
    sum = 0
    negative_numbers = []
    delimiter = string_numbers[2:3]
    for factor in string_numbers[4:].replace('\n',delimiter).split(delimiter):
        sum += int(factor)
    return sum'''
