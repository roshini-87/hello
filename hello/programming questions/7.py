heads = 35
legs = 94
chicken = 0  
while chicken <= heads:
    rabbits = heads - chicken 
    if (2 * chicken) + (4 * rabbits) == legs:
        print(f"Number of chickens: {chicken}")
        print(f"Number of rabbits: {rabbits}")
        break
    chicken += 1 

if chicken > heads:
    print("No solution found.")
