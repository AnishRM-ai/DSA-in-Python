#FInd the middle element of the list.
#if the element on the 
#middle is even, return the average of the two middle elements.
#If the list has an even number of elements, return the average of the two elements in the
#middle.
#element is sorted in a descending order.

test_case0 = {
    "input":{
        "cards": [10, 8,6,4,3,2,1],
        "query": 3,
        } ,
    "output": 4,
    
}

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
        
            
    

def locate_card(cards, query):
    low, high = 0, len(cards) -1
    
    while low <= high:
        mid = (low + high) // 2
        mid_number = cards[mid]
        print("low ", low, "high ", high, "Mid ", mid, "Mid Number ", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            high = mid - 1
        elif mid_number > query:
            low = mid + 1
    return -1
    
print(locate_card(**test_case0['input']) == test_case0['output'])