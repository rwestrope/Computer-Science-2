
nums = []
target = 0
recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    global comparisons, recursions

    recursions += 1
    comparisons += 1    
    if upper >= lower:
        #recursions += 1
        mid = ((upper + lower) // 2)
        comparisons += 1
        if nums[mid] == target:              
            return mid
                
        elif nums[mid] > target:  
            comparisons += 1      
            #recursions += 1
            return binary_search(nums, target, lower, mid - 1)
        
        elif nums[mid] < target: 
            comparisons += 1   
            #recursions += 1
            return binary_search(nums, target, mid + 1, upper)
        
    else:
        return -1


if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input('input the list of numbers\n:').split()]
    print(nums)

    # Input a target value
    target = int(input('input the target number\n:'))

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')