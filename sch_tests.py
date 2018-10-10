import math
import json
from busyint import *

def gen_tda(in_name, v):
    
    tasks = in_name
    
    ints = busy_int(tasks, v)
    jobs = []
    for i in range(1, len(tasks)):
        jobs.append(math.ceil(ints[i-1]/tasks[i]['period']))
    
    #Iteration
    for i in range(1, len(tasks)):
        for j in range(jobs[i - 1]):
        
            R = tasks[i]['c']
            
            while True:
                R2 = 0
                iter_sum = 0
                for k in range(0, i):
                    iter_sum += math.ceil((R + ((j) * tasks[i]['period']))/tasks[k]['period']) * tasks[k]['c']
                R2 = ((j+1)*tasks[i]['c']) + iter_sum - ((j)*tasks[i]['period'])
                if R2 == R:
                    if v == 1:
                        print("Maximum Response time for Job " + str(j) + " Task " + str(i) + " is " + str(R))
                    if R > tasks[i]['deadline']:
                        if v == 1:
                            print("Test Failed by Job " + str(j) + " Task " + str(i))
                        return False
                        exit()
                    break
                else:
                    #print("Task " + str(i) + " Job " + str(j) + " Response time is " + str(R2))
                    R = R2
    return True

def rta(in_name, v):
    
    tasks = in_name
    
    #Iteration
    for i in range(1, len(tasks)):
        t = 0
        for k in range(i+1):
            t += tasks[k]['c']
            
        while True:
            t2 = 0
            iter_sum = 0
            for j in range(0, i):
                iter_sum += math.ceil(t/tasks[j]['period'])*tasks[j]['c']
            t2 = tasks[i]['c'] + iter_sum
            if t2 == t:
                if v == 1:
                    print("Maximum Response time for Job " + str(j) + " Task " + str(i) + " is " + str(R))
                if R > tasks[i]['deadline']:
                    if v == 1:
                        print("Test Failed by Job " + str(j) + " Task " + str(i))
                    return False
                    exit()
                break
            else:
                #print("Task " + str(i) + " Job " + str(j) + " Response time is " + str(R2))
                t = t2
    return True

def util(tasks, verbose, rm):
    util_val = 0
    for task in tasks:
        util_val += (task['c']/task['period'])
    if verbose == 1:
        print("Utilization for Task Set is " + str(util_val))
    if rm:
        if util_val > len(tasks) * (2**(1/len(tasks) - 1)):
            return False
        else:
            return True
    else:
        if util_val > 1:
            return False
        else:
            return True

def den(tasks, verbose, rm):
    util_val = 0
    for task in tasks:
        util_val += (task['c']/min(task['period'], task['deadline']))
    if verbose == 1:
        print("Utilization for Task Set is " + str(util_val))
    if rm:
        if util_val > len(tasks) * (2**(1/len(tasks)) -1):
            return False
        else:
            return True
    else:
        if util_val > 1:
            return False
        else:
            return True

