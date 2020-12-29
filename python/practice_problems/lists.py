import random


def random_element(a):
    num = random.randint(0, len(a) - 1)
    return a[num]
    
print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'
print(random_element(['apples', 'bananas', 'pears', 'pecans', 'avocado'])) # 'apples', 'bananas' or 'pears'


def eveneven(llama):
    counter = 0
    for num in llama:
        if num % 2 == 0:
            counter += 1
    
    # if counter % 2 == 0:
    #     return True
    # else:
    #     return False
    return counter % 2 == 0

print(eveneven([5, 6, 2])) # True
print(eveneven([5, 5, 2])) # False
print(eveneven([5, 5, 2, 4])) # False


def reverse(panda):
    # panda.reverse()
    # return panda

    # return panda[::-1]

    # panda.sort(reverse=True)
    # return panda
    reversed_panda = []
    while len(panda) > 0:
        reversed_panda.append(panda.pop())
    return reversed_panda

print(reverse([1, 2, 3])) # 3, 2, 1


def extract_less_than_ten(nums):
    # less_than_ten = []
    # for num in nums:
    #     if num < 10:
    #         less_than_ten.append(num)
    # return less_than_ten

    return [num for num in nums if num < 10] # list comprehension

    # less_than_ten = [num for num in nums if num < 10]
    # return less_than_ten

print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]


def common_elements(nums1, nums2):
    # output = []
    # for num in nums1:
    #     if num in nums2:
    #         output.append(num)
    # return output

    return [num for num in nums1 if num in nums2]

print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]


def common_elements3(nums1, nums2, num3):

    return [num for num in nums1 if num in nums2 and num in num3]

print(common_elements3([1, 2, 3], [2, 3, 4], [3, 4, 5])) # [3]


def combine(nums1, nums2):
    # output = []
    # for index in range(len(nums1)):
    #     output.append(nums1[index])
    #     output.append(nums2[index])
    # return output

    # return [num for num in len(nums1) for num in (nums1, nums2)]

    # return [num for num in (str(nums1), nums2) for num in (nums2)]

    output = list(zip(nums1, nums2))
    return output

print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]