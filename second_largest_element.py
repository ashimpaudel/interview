#find the second largest element
this_list = [-1,1,2,3,4,5,6]
max_value = max(this_list)
while max_value == max(this_list):
    this_list.remove(max_value)
print max(this_list)
