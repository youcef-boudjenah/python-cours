nums = input("Enter numbers separated by space: ").split()

nums = [int(n) for n in nums]

highest = max(nums)
lowest = min(nums)
sorted_list = sorted(nums)
average = sum(nums) / len(nums)

print("Highest number:", highest)
print("Lowest number:", lowest)
print("Sorted list:", sorted_list)
print("Average value:", average)
