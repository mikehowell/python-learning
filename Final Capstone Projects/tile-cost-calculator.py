import math

tile_cost = float(input("Please enter the cost of tiles per square metres: "))
room_area = float(input("Please enter the room size in square metres: "))

cost_to_tile = round(room_area * tile_cost, 2)

print("total cost to tile the room is ${}".format(cost_to_tile))
print("")

tile_area = float(input("Please enter the tile size in square centimeters: "))
number_of_tiles_needed = math.ceil((room_area * 10000) / tile_area)

print("Number of tiles needed = {}".format(number_of_tiles_needed))
