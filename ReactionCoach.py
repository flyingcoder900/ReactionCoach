#Command used to install GPIO Library on Pi Zero
##pip install RPi.GPIO


# Create a list of 3 reaction entries to be used.


results = {
    "reaction1": 5 ,
    "reaction2": 10 ,
    "reaction3": 15 ,
}

list = []

for val in results.keys():
    list.append(results[val])
print((sum(list) / 3))











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

#reactions = {}


