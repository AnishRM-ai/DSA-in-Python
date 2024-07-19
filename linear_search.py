"""Algorithm
create a variable postion with value 0,
check the cards in an ascending order,
if the card is not equal to the postion then increment it by 1 until it matches the card till the end,
if not found then return -1.

"""
test_case0 = {
    "input":{
        "cards": [1,4,3,6,4,1,6],
        "query": 3,
        } ,
    "output": 2,
    
}


def find_card(query, cards):
    position = 0
    
    while  cards[position] < len(cards):
        if cards[position]  == query:
            return position
        
        position += 1
        
        if position == len(cards):
            return -1
        
    

print(find_card(**test_case0['input']) == test_case0['output'])