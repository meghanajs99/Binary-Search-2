//Time Complexity: O(logn)
//Space Complexity: O(1)

//code
 if len(nums)==1:
    return nums[0]
        
  low=0
  high=len(nums)-1

  if nums[high]>nums[0]:
      return nums[0]

  while(low<=high):

      mid=low+(high-low)//2

      if (nums[mid]>nums[mid+1]): //if mid element is greater than its right neighbor the minimum element must be the right neighbor because the array is sorted
          return nums[mid+1]

      if nums[mid-1]>nums[mid]:  //if mid element is less than the left neighbor the mid element is the minimum element 
          return nums[mid]

      if nums[mid]>nums[0]: // if mid element is greater than the first element the minimum element must be after the mid element 
          low=mid+1
      else:
          high=mid-1 //else the minimum element must be before the mid element
