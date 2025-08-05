#WAP to calculate total cost of painting . the interior of building with four equal sized walls.

cost = int(input("Enter the cost of one side wall : "))
side = int(input("Enter the size of one wall : "))

total_wall_size = side*4

tot_cost = cost *total_wall_size

print(f"Total cost of painting : {tot_cost}") 