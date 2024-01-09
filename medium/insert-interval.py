# https://leetcode.com/problems/insert-interval/description/


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        def Solution2(intervals, newInterval):
            # we will create a new array, and add the intervals that does not overlap, one by one. For the ones that overlap with newInterval, we have to treat it. If we get to know that there won't be any overlapping, so we have just to add the newInterval to the new array. time O(n). space O(n). Maybe an approach that do a binary search would be faster, however we may still need to add and remove elements, making the time complexity still O(n).

            # include start
            start = newInterval[0]
            end = newInterval[1]
            new_intervals = []
            overlap = False
            intervals.insert(
                0, [-1000000, -1000000]
            )  # adding this, the algorithm will work for special cases such an empty list
            intervals.append([1000000, 1000000])

            for i in range(0, len(intervals)):
                # searching for everlaps
                if start > intervals[i][1] or end < intervals[i][0]:  # no overlap
                    if (
                        overlap == True
                    ):  # we were in the overlap condition, and now it des-overlaped. So we need to add the new interval given by [start,end]
                        new_intervals.append([start, end])
                    new_intervals.append(
                        intervals[i]
                    )  # no overlaping, so we add the pair to the new_intervals
                    overlap = False
                else:  # overlaps
                    start = min(
                        start, intervals[i][0]
                    )  # update the start, once newInterval[0] is overlaping with it
                    end = max(
                        end, intervals[i][1]
                    )  # update the end, once newInterval[0] is overlaping with it
                    overlap = True
                    # note that we will not add the intervals[i] to the new_intervals

                if (
                    start > intervals[i][1] and end < intervals[i + 1][0]
                ):  # the newInterval will never lead to an overlaping condition. Thus we need to add it to new_intervals
                    new_intervals.append(newInterval)

            if intervals == []:
                new_intervals.append(newInterval)

            return new_intervals[
                1:-1
            ]  # remove the pairs[-1000000, -1000000] and [1000000, 1000000]

        return Solution2(intervals, newInterval)
