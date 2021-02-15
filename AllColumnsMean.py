#!/usr/bin/python

from mrjob.job import MRJob
from mrjob.step import MRStep


class MRAllColumnsMean(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_sum),
            MRStep(reducer=self.reducer_average)
        ]

    def mapper(self, _, line):
        column = 0
        for i in range(12):
            value = line.split()[i]
            column += 1
            if value[0].isdigit() or value[0] == '-':
                yield column, (float(value))

    def reducer_sum(self, key, pairs):
        total = 0
        counts = 0
        for value in pairs:
            total += value
            counts += 1
        yield key, (counts, total)

    def reducer_average(self, key, pairs):
        valueSum = 0
        countSum = 0
        for value in pairs:
            valueSum += value[1]
            countSum += value[0]
        yield key, valueSum / countSum


if __name__ == '__main__':
    MRAllColumnsMean.run()
