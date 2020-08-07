#my solution - Time complexity O(n^2)
def intersection(nums1, nums2):
    output = set()

    for i in range(len(nums2)):
        if nums2[i] not in output:
            if nums2[i] in nums1:
                output.add(nums2[i])
    return output

#leetcode solution #1

def set_intersection(self, set1, set2):
    return [x for x in set1 if x in set2]

def soln1_intersection( nums1, nums2):

    set1 = set(nums1)
    set2 = set(nums2)

    if len(set1) < len(set2):
        return set_intersection(set1, set2)
    else:
        return set_intersection(set2, set1)


def soln2_intersection(nums1, nums2):

    set1 = set(nums1)
    set2 = set(nums2)
    return list(set2 & set1)

