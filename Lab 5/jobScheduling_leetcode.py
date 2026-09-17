class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):

        jobs = []

        for i in range(len(startTime)):
            jobs.append((startTime[i], endTime[i], profit[i]))

        jobs.sort(key=lambda x: x[1])

        end_times = [job[1] for job in jobs]

        dp = [0] * (len(jobs) + 1)

        for i in range(1, len(jobs) + 1):

            start = jobs[i - 1][0]
            current_profit = jobs[i - 1][2]

            j = bisect_right(end_times, start, 0, i - 1)

            skip = dp[i - 1]
            take = current_profit + dp[j]

            dp[i] = max(skip, take)

        return dp[-1]
