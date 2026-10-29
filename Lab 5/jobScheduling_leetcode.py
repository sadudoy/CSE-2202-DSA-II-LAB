# class Solution(object):
#     def jobScheduling(self, startTime, endTime, profit):

#         jobs = []

#         for i in range(len(startTime)):
#             jobs.append((startTime[i], endTime[i], profit[i]))

#         jobs.sort(key=lambda x: x[1])

#         end_times = [job[1] for job in jobs]

#         dp = [0] * (len(jobs) + 1)

#         for i in range(1, len(jobs) + 1):

#             start = jobs[i - 1][0]
#             current_profit = jobs[i - 1][2]

#             j = bisect_right(end_times, start, 0, i - 1)

#             skip = dp[i - 1]
#             take = current_profit + dp[j]

#             dp[i] = max(skip, take)

#         return dp[-1]





class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # 1. Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # 2. Find the maximum deadline to size the time slot array
    max_deadline = max(job.deadline for job in jobs)
    
    # Track available time slots (True means the slot is filled)
    # Size is max_deadline + 1 to use 1-based indexing for days
    slots = [False] * (max_deadline + 1)
    scheduled_jobs = [''] * (max_deadline + 1)
    
    total_profit = 0
    jobs_done = 0
    
    # 3. Iterate through jobs to schedule them
    for job in jobs:
        # Check for free slots starting from the job's deadline, working backward
        for j in range(job.deadline, 0, -1):
            if not slots[j]:  # If slot is free
                slots[j] = True
                scheduled_jobs[j] = job.job_id
                total_profit += job.profit
                jobs_done += 1
                break  # Move to the next job once scheduled
                
    # Filter out empty slots for the final execution sequence
    sequence = [job for job in scheduled_jobs if job != '']
    
    return sequence, jobs_done, total_profit

# --- Example Usage ---
# Format: Job(ID, Deadline, Profit)
job_list = [
    Job('J1', 2, 100),
    Job('J2', 1, 19),
    Job('J3', 2, 27),
    Job('J4', 1, 25),
    Job('J5', 3, 15)
]

sequence, count, profit = job_scheduling(job_list)

print(f"Execution Sequence: {sequence}")
print(f"Total Jobs Completed: {count}")
print(f"Maximum Profit: {profit}")