#solve this in 17 minutes
#python

def two_sum(list, k):
    Found = False
    
    for i in range (len(list)-1):
        for j in range (len(list)-1):
            if list[i] + list [j]  == k:
                ketemu = True
                break

        if ketemu == True:
            break
            
    return ketemu  
    
  # Fill this in.

print ( two_sum([4,7,1,-3,2], 5) )
# True
def two_sum(list, k):
    Found = False
    
    for i in range (len(list)-1):
        for j in range (len(list)-1):
            if list[i] + list [j]  == k:
                ketemu = True
                break

        if ketemu == True:
            break
            
    return ketemu  
    
print ( two_sum([4,7,1,-3,2], 5) )
