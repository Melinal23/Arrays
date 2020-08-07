def merge_student_soln(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    small = len(nums2) - 1

    big = len(nums1) - len(nums2) - 1

    runner = len(nums1) - 1

    while (small >= 0 and big >= 0):
        if nums1[big] > nums2[small]:
            nums1[runner] = nums1[big]
            runner -= 1
            big -= 1
        else:
            nums1[runner] = nums2[small]
            small -= 1
            runner -= 1

    if big < 0 and small >= 0:
        while small >= 0:
            nums1[runner] = nums2[small]
            runner -= 1
            small -= 1

def merge(nums1, m, nums2, n):

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        m -= 1
        n -= 1