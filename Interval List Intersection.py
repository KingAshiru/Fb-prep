class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1 = ptr2 = 0
        answer = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            low = max(firstList[ptr1][0], secondList[ptr2][0])
            high = min(firstList[ptr1][1], secondList[ptr2][1])
            if low <= high:
                answer.append([low, high])
            if firstList[ptr1][1] > secondList[ptr2][1]:
                ptr2 += 1
            else:
                ptr1 += 1
        return answer
