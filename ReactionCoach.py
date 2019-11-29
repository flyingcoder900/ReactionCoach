# Command used to install GPIO Library on Pi Zero
# pip install RPi.GPIO
# import statistics
# Create a list of 3 reaction entries to be used.
# Runs the function to get a reaction time

results = []


while True:
    reaction_count = len(results)
    if reaction_count <= 2:
        run = input("Enter a reaction time: ")
        results.append(int(run))
        reaction_count += 1
        print(results)
        print("Reaction count is ", reaction_count)
        continue
    else:
        reaction_count = 0
        results.sort()
        print(results)
        variance = int(results[2] - results[0])
        print(variance)
        results = []
    # else:
    #     reaction_spread = float(input("Enter a reaction spread: "))
    #     if reaction_spread <= .015:
    #             # three LED flashes
    #             print("Three Led Flashes")
    #     if .016 <= reaction_spread <= .030:
    #             # two Led Flashes
    #             print("Two Led Flashes")
    #     if reaction_spread >= .031:
    #             # One Led Flash
    #             print("One Led Flash")
    #     results = []
# list = 0

# def get_reaction_average():
    # for val in results.values():
        # list.append(results[val]

# program Green LED Ready Light.

# Wait for button press from the user.

# Press button.


# Wait a random amount of time that is deemed normal from watching a race and calculating an average.

# If button still pressed then flash light and note time in library place one.
# If button not pressed then start back at beginning and light green ready light.
# repeat process until all 3
# Calculate the total time range

# If X =< .015 then flash 3 times.
# If .015 > X >= .025 then flash 2 times.
# If x > .025 then flash 1 time.
# Reset game
# reactions = {}
