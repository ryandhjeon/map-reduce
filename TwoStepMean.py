#!/usr/bin/python

from mrjob.job import MRJob
from mrjob.step import MRStep


class MRCalculateMeanTask2(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_partition_items,
                   reducer=self.reducer_sum),
            MRStep(mapper=self.mapper_empty,
                   reducer=self.reducer_get_average)
        ]

    def mapper_partition_items(self, _, line):
        value = line.split()[3]
        num_item = 0
        if value[0].isdigit():
            for x in value:
                num_item += 1
            yield None, float(value)

    def reducer_sum(self, _, values):
        counts = 0
        total = 0
        for p in values:
            counts += 1
            total += p
        yield None, (counts, total)

    def mapper_empty(self, _, pairs):
        yield None, pairs

    def reducer_get_average(self, _, pairs):
        sum_values = 0
        sum_count = 0
        for p in pairs:
            sum_values += p[1]
            sum_count += p[0]
        yield "Mean", sum_values/sum_count


if __name__ == '__main__':
    MRCalculateMeanTask2.run()