# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:01:52 2020

@author: Vitor
"""

import numpy as np
# Read and parse input
f = open("input.txt", "r")
inputs = list(map(int, f.read().split()))
f.close()
ttask, umax, new_users = inputs[0], inputs[1], inputs[2:] 
new_users += [0]*ttask   #complete new_users list

def add_user():
    '''
    Assign user to server and initiates its countdown
    '''
    global countdown
    # check available servers
    priority = [max(i) if len(i) < umax else 0 for i in countdown]
    if any(priority):
        # Assing user to server with longest lifetime
        index = np.argsort(priority)[-1]
        countdown[index].append(ttask)
    else:
        # Assign user to new server
        countdown.append([ttask])

def tick():
    # Tick takes effect, removing finished users and/or 
    # servers and decreasing countdown for the remaining ones
    global countdown
    temp_list = []
    for sublist in countdown:
        temp = [value-1 for value in sublist if value-1 > 0]
        if temp: temp_list.append(temp)
    countdown = temp_list
        
    
countdown = []
total = []
# Main loop
for users in new_users:
    tick()
    for i in range(users):
        add_user()
    total.append([len(i) for i in countdown if i])
    
total.append([sum([len(i) for i in total])])    #calculates total
total = [i if i else [0] for i in total]        #convert empty to 0

with open('output.txt', 'w') as f:
    for i in total: f.write(','.join(map(str, i)) + '\n')
    f.close()

#print(*total, sep='\n')


