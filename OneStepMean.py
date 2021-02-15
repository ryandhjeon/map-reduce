#!/usr/bin/python

from mrjob.job import MRJob


class MRCalculateMean(MRJob):

    def mapper(self, _, line):
        value = line.split()[3]
        if (value[0].isdigit()):
            yield None, float(value)

    def reducer(self, key, values):
        sum_keys = 0
        sum_values = 0
        for value in values:
            sum_values += value
            sum_keys += 1
        yield None, sum_values / sum_keys


if __name__ == '__main__':
    MRCalculateMean.run()