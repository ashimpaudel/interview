#window problem
my_list = [1,2,3,4,5,6,7,8,9]
window = 3
first_index = 0
last_index = window
for i in range(len(my_list)/window):
    print sum(my_list[first_index:last_index])/window
    print first_index, window
    first_index = last_index
    last_index += window
    
