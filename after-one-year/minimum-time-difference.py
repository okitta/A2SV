class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 24*60:
            return 0
        time = []
        for timepoint in timePoints:
            hr,m = timepoint.split(':')
            time.append(int(hr)*60+int(m))
        print(time)
        time.sort()
        min_diff = time[0] + 24*60 - time[-1]
        for idx in range(len(time)-1):
            min_diff = min(min_diff,time[idx+1] - time[idx])
        
        return min_diff