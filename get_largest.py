nums = []
in_list = input("Enter number separated by space(Eg:4 5 5 5): ")
in_list = in_list.split()
nums.extend(list(map(int,in_list))) #Insert numbers into list after typecast
smallest = float('inf') #for positive infinity so every number is smaller    
largest = float('-inf') #for negative infinity so every number is greater
is_add = input("Would you like to add another number?(y/n): ")
while is_add.lower() == 'y':
    add_num = int(input("Add one number: "))
    nums.append(add_num)
    is_add = input("Would you like to add another number?(y/n): ")
    
for i in nums: #Iteration over all the numbers entered
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i

print(f'List of numbers: {nums} Minimum: {smallest} Maximum: {largest}')

print('\nAlternative code here using list min() and max()')
print(f'List of numbers: {nums} Minimum: {min(nums)} Maximum: {max(nums)}')