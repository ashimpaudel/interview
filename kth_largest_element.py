#find the kth largest value
this_list = [1,2,3,4,5,6,6,7,8,8,8]
k = 5
for i in range(k-1):
    max_value = max(this_list)
    while max_value == max(this_list):
        this_list.remove(max_value)
print max(this_list)
