class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students = 0

        for s, e in zip(startTime, endTime):
            diff = {*range(s, e + 1)}
            if queryTime in diff:
                students += 1

        return students