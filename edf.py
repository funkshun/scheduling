import json
import sys

def addExecution(out_data, task, job, start, end):
    sample = {}
    sample['taskNum'] = task
    sample['jobNum'] = job
    sample['start'] = start
    sample['end'] = end
    out_data['executions'].append(sample)

def addToJobList(jobList, taskNum, jobNum, release, deadline, c):
    temp = {}
    temp['taskNum'] = taskNum
    temp['jobNum'] = jobNum
    temp['release'] = release
    temp['deadline'] = deadline
    temp['c'] = c
    jobList.append(temp)
    
def findMaxDeadline(jobList):
    maxDeadline = 0
    for job in jobList:
        if job['deadline'] > maxDeadline:
            maxDeadline = job['deadline']
    return maxDeadline

def findMaxTaskNum(tasks):
    maxTaskNum = tasks[0]['num']
    for task in tasks:
        if task['num'] > maxTaskNum:
            maxTaskNum = task['num']
    return maxTaskNum

def edf(tasks, t, out_name):

    tasks = tasks
    max_t = t
    
    out_data = {}
    out_data['max_t'] = max_t
    out_data['tasks'] = tasks
    out_data['executions'] = []

    # Create a list of all jobs
    jobList = []
    for task in tasks:
        temp_time = task['phase']
        jobNum = 0
        while temp_time < max_t:
            addToJobList(jobList,
                        task['num'],
                        jobNum,
                        temp_time,
                        temp_time+task['deadline'],
                        task['c'])
            temp_time = temp_time + task['period']
            jobNum = jobNum + 1

    # Add executions based on EDF
    executions = out_data['executions']
    maxDeadline = findMaxDeadline(jobList) + 1
    maxTaskNum = findMaxTaskNum(tasks)
    time = 0
    while (time < max_t):
        if jobList == []:
            break

        earliestJob = None
        earliest_deadline = maxDeadline
        earliest_taskNum = maxTaskNum

        # Find job to execute next
        for job in jobList:
            if (job['release'] <= time 
                    and (job['deadline'] < earliest_deadline
                    or (job['deadline'] == earliest_deadline
                    and job['taskNum'] <= earliest_taskNum))):
                earliest_deadline = job['deadline']
                earliestJob = job
                earliest_taskNum = job['taskNum']

        # If there is a job to execute, add one time unit of execution
        if earliestJob != None:
            if (executions != [] 
                    and executions[-1]['taskNum'] == earliestJob['taskNum'] 
                    and executions[-1]['jobNum'] == earliestJob['jobNum']):
                executions[-1]['end'] = time+1
            else:
                addExecution(out_data,
                        earliestJob['taskNum'],
                        earliestJob['jobNum'],
                        time,
                        time+1)
            earliestJob['c'] = earliestJob['c'] - 1
            if earliestJob['c'] == 0:
                jobList.remove(earliestJob)
        time = time + 1

    with open(out_name, 'w') as out_file:  
        json.dump(out_data, out_file)
    return out_name
