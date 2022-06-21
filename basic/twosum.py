def twoSum(nums, target):
# solution 1: O(n*n)
# first_ind = 0 
# while first_ind < len(nums):
#     result = target - nums[first_ind]
#     if result in nums:
#         second_ind = nums.index(result)
#         if second_ind != first_ind: 
#             return [first_ind, second_ind]
#     first_ind += 1

# solution 2: O(n*logn)
  nums_ind = []
  for i in range(len(nums)):
    nums_ind.append([nums[i],i])
  nums_ind.sort()
  sorted_ind = []
  for i in range(len(nums_ind)):
    sorted_ind.append(nums_ind[i][1])
  print(nums_ind)
  print(sorted_ind)
  first_ind = 0
  while first_ind < len(nums_ind):
    result = target - nums_ind[first_ind][0]
    lower_ind = 0
    upper_ind = len(nums_ind)-1
    middle = (lower_ind + upper_ind)//2
    print([result, nums_ind[middle][0]])
    print([lower_ind, upper_ind, middle])
    step = 0
    while lower_ind != upper_ind:
      print([result, nums_ind[middle][0]])
      print([lower_ind, upper_ind, middle])
      if result > nums_ind[middle][0]:
        lower_ind = middle
        middle = (lower_ind + upper_ind)//2 + 1
        if middle == len(nums_ind)-1:
          break
      elif result < nums_ind[middle][0]:
        upper_ind = middle
        middle = (lower_ind + upper_ind)//2 
        if middle == 0:
          break
      else: # result == nums_ind[middle][0]
        if middle != first_ind:
          return [sorted_ind[first_ind], sorted_ind[middle]]
        else:
          break
      if step <= math.log2(len(nums_ind))+1:
        step += 1
      else:
        break
    first_ind += 1

# solution 3: O(n)
#  nums_ind_dict = {}
#  ind = 0
#  for num in nums:
#    if num in nums_ind_dict:
#      nums_ind_dict[num].append(ind)
#    else:
#      nums_ind_dict[num] = [ind]
#    ind += 1
#  for num in nums:
#    result = target - num
#    if result in nums_ind_dict:
#      if len(nums_ind_dict[result]) == 1:
#        if nums_ind_dict[num][0] !=  nums_ind_dict[result][0]:
#          return [nums_ind_dict[num][0], nums_ind_dict[result][0]]
#      elif len(nums_ind_dict[result]) == 2:
#        return [nums_ind_dict[num][0], nums_ind_dict[result][1]]

def main():
  nums = [2,5,5,11]
  target = 10
  ind  = twoSum(nums, target)
  if ind is not None:
    print("indies = [%d %d]" % (ind[0], ind[1]))

if __name__ == '__main__':
  main()
