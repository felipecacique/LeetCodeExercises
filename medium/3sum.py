class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution1: we will add the nums to a set, as we do the 2 for loops with the set, geting values a and b (O(n^2)). Notice that the formula can be a+b+c=0  or a+b=-c. Using the last one, we search for -c in the set (O(1)). So our time complexity will be O(n^2), and space O(n).

        def Solution1(nums):
            # O(n^2)
            solution = set()
            seen = set()

            s = set()
            for i in range(1, len(nums)):
                for j in range(i + 1, len(nums)):
                    s.add(
                        nums[i - 1]
                    )  # add the value before. So that the s will always correspond to nums with index before the a and b indexes. So we can make sure thay the tuplet indexes are all different
                    a = nums[i]
                    b = nums[j]
                    c = -(a + b)
                    # if we can fing c in the set, then we have a triplet
                    if c in s:
                        # solution.append([a,b,c])

                        # # this part is for saving the seen solutions in a set, and avoid duplicate triplets
                        # sol_string = ''
                        # for num in sorted([a,b,c]):
                        #     sol_string = sol_string + str(num) + ' '

                        # if not sol_string in seen:
                        #     seen.add(sol_string)
                        #     solution.append([a,b,c]) # if we havent seen this triplet yet, then we add it to the solution

                        solution.add(tuple(sorted([a, b, c])))

            return solution

        def Solution2(nums):  # same solution as 1, but a bit optimized
            # O(n^2) optimized
            solution = []
            seen = set()

            # lets work with a sorted array
            nums = sorted(nums)
            idx_start_positive = 0
            for i, num in enumerate(nums):
                if num >= 0:
                    idx_start_positive = i
                    break

            s = set()
            for i in range(1, len(nums)):
                # note that nums[k] (our harsh) will contain numbers < than nums[i]. In this loop, for each iteraction our triples will given by [nums[k], nums[i], nums[j]]. For nums[i] <=0, since nums[k] <= nums[i], then nums[j] >= 2*nums[i] otherwise it would be impossible for having a sum == 0. We will handle this by iterating j reversely, from the highest values to the lowest, and then breaking the loop when nums[j] < 2*nums[i]. ***
                for j in reversed(
                    range(max(i + 1, idx_start_positive), len(nums))
                ):  # i and k ar negative, j must be pointing to positive numbers, otherwise it will never give sum == 0. Thus we start j in the index idx_start_positive, for i pointing to negative values. And when i is pointing to positive values, j is i+1 (such as before). This way we prune some unecessary iterations.
                    s.add(
                        nums[i - 1]
                    )  # add the value before. So that the s will always correspond to nums with index before the a and b indexes. So we can make sure thay the tuplet indexes are all different

                    if nums[j] < -2 * nums[i]:  # ***
                        break

                    # if nums[i] <= 0:
                    #     if nums[j] > -2*nums[0]:

                    a = nums[i]
                    b = nums[j]
                    c = -(a + b)
                    # if we can fing c in the set, then we have a triplet
                    if c in s:
                        # solution.append([a,b,c])

                        # this part is for saving the seen solutions in a set, and avoid duplicate triplets
                        sol_string = ""
                        for num in sorted([a, b, c]):
                            sol_string = sol_string + str(num) + " "

                        if not sol_string in seen:
                            seen.add(sol_string)
                            solution.append(
                                [a, b, c]
                            )  # if we havent seen this triplet yet, then we add it to the solution

            return solution

        def Solution3(nums):
            # O(n^2) optimized ... still not good .... Solution1 is still the better.
            solution = []
            seen = set()

            # lets work with a sorted array
            nums = sorted(nums)
            pos_nums = []
            neg_nums = []
            s = {}
            idx_start_positive = 0
            for i, num in enumerate(nums):
                if num >= 0:
                    idx_start_positive = i
                    break

            for i, num in enumerate(nums):
                if not num in s:
                    s[num] = set()
                    s[num].add(
                        i
                    )  # store the nums and its ids. Since the number can be duplicated in nums, we store all the ids where it apprears, in a set()
                else:
                    s[num].add(i)

            # if idx_start_positive == 0:  # you cannot have sum == 0 with only negative nums
            #     return []

            print(nums)
            # for each 2 neg nums, we have to look for a positive number
            for i in reversed(range(0, idx_start_positive)):
                for j in reversed(range(0, i)):
                    a = nums[i]
                    b = nums[j]
                    if -(a + b) > nums[-1]:
                        break

                    c = -(a + b)

                    # if we can fing c in the set, then we have a triplet
                    if c in s:
                        if (
                            ((i in s[c]) and not (j in s[c]) and len(s[c]) > 1)
                            or ((j in s[c]) and not (i in s[c]) and len(s[c]) > 1)
                            or ((i in s[c]) and (j in s[c]) and len(s[c]) > 2)
                            or (not (i in s[c]) and not (j in s[c]) and len(s[c]) >= 0)
                        ):  # make sure they all have unique ids
                            # if not i in s[c] and not j in s[c]: # make sure they all have unique ids
                            # solution.append([a,b,c])
                            # this part is for saving the seen solutions in a set, and avoid duplicate triplets
                            sol_string = ""
                            for num in sorted([a, b, c]):
                                sol_string = sol_string + str(num) + " "

                            if not sol_string in seen:
                                seen.add(sol_string)
                                solution.append([a, b, c])

            # for each 2 pos nums, we have to look for a negative number
            len_nums = len(nums)
            for i in range(idx_start_positive, len_nums - 1):
                for j in range(i + 1, len_nums):
                    a = nums[i]
                    b = nums[j]
                    if (a + b) > -nums[0]:
                        break

                    c = -(a + b)

                    # if we can fing c in the set, then we have a triplet
                    if c in s:
                        if (
                            ((i in s[c]) and not (j in s[c]) and len(s[c]) > 1)
                            or ((j in s[c]) and not (i in s[c]) and len(s[c]) > 1)
                            or ((i in s[c]) and (j in s[c]) and len(s[c]) > 2)
                            or (not (i in s[c]) and not (j in s[c]) and len(s[c]) >= 0)
                        ):  # make sure they all have unique ids
                            # if not i in s[c] and not j in s[c]: # make sure they all have unique ids
                            # solution.append([a,b,c])
                            # this part is for saving the seen solutions in a set, and avoid duplicate triplets
                            sol_string = ""
                            for num in sorted([a, b, c]):
                                sol_string = sol_string + str(num) + " "

                            if not sol_string in seen:
                                seen.add(sol_string)
                                solution.append([a, b, c])

            return solution

        def Solution4(nums):
            # solution using pointers left and right. time O(n^2) but it is faster than the SOLUTION1. same as https://www.youtube.com/watch?v=cRBSOz49fQk&ab_channel=NikhilLohia . Lthough it is the same complexity as the Solution1, we could optmize a little bit like skipping repeated values, skipping when the three number are positive intergers ...

            solution = set()
            nums.sort()

            for k in range(0, len(nums) - 2):
                if nums[k] > 0:  # skip positive integers
                    break

                if (
                    k > 0 and nums[k] == nums[k - 1]
                ):  # skip repeated values (improved time in 2x)
                    continue

                sum = -nums[k]

                # now it became the problem of 2sum, where we have to find a+b = sum
                left = k + 1
                right = len(nums) - 1

                while left < right:
                    if nums[left] + nums[right] < sum:
                        left += 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        solution.add((nums[k], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1

            return solution

        return Solution4(nums)
