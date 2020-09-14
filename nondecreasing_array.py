def non_decreasing_array(nums):

        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return True

        prev = 0
        change_count = 0

        for i in range(len(nums) - 1):

            if nums[i] > nums[i + 1]:  # decreasing array
                change_count += 1  # increment the count for num of changes to make
                if change_count > 1:
                    return False
                elif prev > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]

            prev = nums[i]

        return True
