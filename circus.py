 #!/usr/bin/env python
"""This script prompts a user to enter a message to encode or decode
1using a classic Caeser shift substitution (3 letter shift)"""
import random
# pylint: disable=invalid-name
performances = {'Ventriloquism':'9:00am',
                'Snake Charmer': '12:00pm',
                'Amazing Acrobatics': '2:00pm',
                'Enchanted Elephants':'5:00pm'}
#for show, time in performances.items():
    #print(show, ":", time)
schedule_file = open('schedule.txt', 'w')
for key, val in performances.items():
    schedule_file.write(key + '-' + val +'\n')
schedule_file.close()
try:
    schedule_file = open('schedule.txt', 'r')
except FileNotFoundError as err:
    print(err)
performances = {}
showlist = []
for line in schedule_file:
    (show, time) = line.split('-')
    #for show, time in performances:
        #showlist = line.split('-')
        #performances[showlist[0]] = showlist[1]
    performances[show] = time.strip()
        
    #print(line)
schedule_file.close()
print(performances)
