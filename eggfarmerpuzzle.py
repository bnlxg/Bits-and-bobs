# The Egg Farmer's Puzzle - www.101computing.net/the-egg-farmer-puzzle/

# Can be solved with math or for-loops
# This is the math solution

# The Egg Farmer's Puzzle - www.101computing.net/the-egg-farmer-puzzle/

#Complete your code here...
print("How many eggs did you get today, Farmer?")
eggs = int(input())

cartons = 12

cartons_math = eggs / 12
cartons_needed = int(cartons_math)
cartons_overflow = eggs - (cartons_needed * 12)

boxes = 6
boxes_math = cartons_overflow / 6
boxes_needed = int(boxes_math)
box_overflow = cartons_overflow - (boxes_needed * 6)

if cartons_overflow > 6:    
    print("You can bring: " + str(cartons_needed) + " cartons and " + str(boxes_needed) + " boxes, and eat " +
          str(int(box_overflow)) + " for breakfast!")

else:
    print("You can bring: " + str(cartons_needed) + " cartons and eat " +
          str(int(box_overflow)) + " for breakfast!")

