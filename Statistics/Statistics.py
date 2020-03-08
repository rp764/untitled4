from Calculator.Calculator import Calculator
from Statistics.Mean import mean

from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def mean(data):
        num_values=len(data)
        total=0
        for num in data:
            total = addiiton(total.num)
            return division(total,num_values)
    def