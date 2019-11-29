
from time import time as the_timer
import datetime
import random
import time

now = datetime.datetime.now()
print(str(now))

# print("current year: {}".format(now.year))
# print("current month: {}".format(now.strftime("%B")))
# print("current day: {}".format(now.strftime("%A")))
# print("current hour: {}".format(now.strftime("%H")))
# print("current minute: {}".format(now.strftime("%M")))

results = []

while True:
    input("Press enter when ready! Reaction: " + str(len(results) + 1))

    wait_time = random.randint(1, 1)
    time.sleep(wait_time)
    start_time = the_timer()

    input("STOP")

    end_time = the_timer()

    # print("Started at " + time.strftime("%X", time.localtime(start_time)))
    # print("Ended at " + time.strftime("%X", time.localtime(end_time)))

    run = format(end_time - start_time)
    results.append(run)
    if len(results) == 3:
        results.sort()
        print(results)
        high_time = float(results[2])
        print(high_time)
        low_time = float(results[0])
        reaction_variance = round((high_time - low_time), 3)

        if reaction_variance <= .015:

            # three LED flashes
            print("Three Led Flashes")
        if .016 <= reaction_variance <= .030:
            # two Led Flashes
            print("Two Led Flashes")
        if reaction_variance >= .031:
            # One Led Flash
            print("One Led Flash")
        print("Your reaction variance: " + str(reaction_variance))
        results = []
        time.sleep(.3)
