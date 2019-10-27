import time
from time import time as the_timer
import datetime
import random
import time

now = datetime.datetime.now()
print(str(now))

#print("current year: {}".format(now.year))
#print("current month: {}".format(now.strftime("%B")))
#print("current day: {}".format(now.strftime("%A")))
#print("current hour: {}".format(now.strftime("%H")))
#print("current minute: {}".format(now.strftime("%M")))

results = []

while True:
    input("Please press enter to start")

    wait_time = random.randint(1,1)
    time.sleep(wait_time)
    start_time = the_timer()

    input("Please press enter to stop")

    end_time = the_timer()

    #print("Started at " + time.strftime("%X", time.localtime(start_time)))
    #print("Ended at " + time.strftime("%X", time.localtime(end_time)))

    run = format(end_time - start_time)
    results.append(run)
    if len(results) == 3:
        results.sort()
        print(results)
        high_time = float(results[2])
        low_time = float(results[0])
        reaction_variance = high_time - low_time
        print(results)
        print("Your variance was: " + str(reaction_variance))
        results = []
