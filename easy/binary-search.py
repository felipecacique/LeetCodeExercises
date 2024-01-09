# https://leetcode.com/problems/binary-search/description/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Lets do the binary search

        def Solution1(nums):
            # recursive

            def binarySearch(nums, i_start, i_end):
                # stop criterion
                if len(nums) == 0:
                    return -1  # no solution
                if len(nums) == 1:
                    if nums[0] == target:
                        return i_start
                    else:
                        return -1  # no solution

                if (
                    target <= nums[int(len(nums) / 2) - 1]
                ):  # the target must be in the left side
                    i = binarySearch(
                        nums[: int(len(nums) / 2)],
                        i_start,
                        i_start + int(len(nums) / 2),
                    )
                else:  # the target must be in the right side
                    i = binarySearch(
                        nums[int(len(nums) / 2) :], i_start + int(len(nums) / 2), i_end
                    )

                return i

            return binarySearch(nums, 0, len(nums))

        # def Solution2(): # iterative

        return Solution1(nums)
