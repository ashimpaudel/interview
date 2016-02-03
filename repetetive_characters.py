#deleting the repetetive characters
a = 'Biiiishwwwwa'
new_string = ''

for i in range(len(a)):
    if i != len(a) -1 and a[i+1] == a[i]:
        pass
    else:
        new_string += a[i]
        
    
print new_string
