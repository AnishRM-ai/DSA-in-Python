"""Algorithm
create a variable postion with value 0,
check the cards in an ascending order,
if the card is not equal to the postion then increment it by 1 until it matches the card till the end,
if not found then return -1.

"""
def find_card(query, cards):
    position = 0
    
    while True:
        if cards[position]  == query:
            return position
        
        position += 1
        
        if position == len(cards):
            return -1
        
    

query = 3
cards = [1,5,2,7,3,9]
print(find_card(query, cards))