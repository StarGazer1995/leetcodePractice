class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        col = len(prerequisites)
        row = len(prerequisites[0])
        start_time = row[0]
        end_time = 0;

        for i in prerequisites:
            start_time = min(start_time,i[0])
            end_time = max(end_time,i[1])
        duration = [0]*(end_time - start_time)

        for i in prerequisites:
            duration[i[0]:i[1]] += 1

        return max(duration)

col =[[1,2],[1,3]]
print(Solution().canFinish(col))
