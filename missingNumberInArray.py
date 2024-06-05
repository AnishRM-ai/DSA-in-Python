
def missingNumber(array,n):
    total_sum = n * (n+1) // 2 #calculating the total sum of n numbers
    array_sum = sum(array) #using sum function to calculate the sum of array.
    missing_number = total_sum - array_sum #finding the missing number.
        
    return missing_number
    
array = [1,3,5,2]
n = 5
print(missingNumber(array,n))