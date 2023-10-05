print("containers:lists")
nums=list(range(5))
print("list'nums' contain:",nums)
nums[4]="abc"
print("list can contain elements of different types.example:",nums)
nums.append("xyz")
print("'nums'after inserting new element at end")
print("sublist:")
print("a slice from index 2 to 4:",nums[2:4])
print("a slice from index 2 to the end:",nums[2:])
print("a slice from start to 2",nums[:2])
print("a slice of whole list:",nums[:])
nums[4:]=[8,9]#assign a new sublist to slice
print("after assigning a new sublist to 'nums'")
for idx,i in enumerate(nums):
        print('%d:%s'%(idx+1,i))
even_squares=[x**2 for x in nums if x % 2==0]
print("list of squares of evennumbers from 'nums'",even_squares)