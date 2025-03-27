# The Egg Farmer's Puzzle - www.101computing.net/the-egg-farmer-puzzle/

# Can be solved with math or for-loops
# This is the loop solution

print("How many eggs did you get today, Farmer?")
eggs = int(input())

carton_size = 12
box_size = 6

cartons_needed = 0
boxes_needed = 0
eggs_remaining = eggs

for i in range(eggs // carton_size):
    cartons_needed += 1
    eggs_remaining -= carton_size

if eggs_remaining > box_size:
    for i in range(eggs_remaining // box_size):
        boxes_needed += 1
        eggs_remaining -= box_size

if boxes_needed > 0:
    print(
        "You can bring: " + str(cartons_needed) + " cartons and " + str(boxes_needed) + " boxes, and eat " + str(eggs_remaining) +
        " for breakfast!")
else:
    print(
        "The eggs fit perfectly in " + str(cartons_needed) + " cartons and you can eat " + str(eggs_remaining) + " for breakfast!")
