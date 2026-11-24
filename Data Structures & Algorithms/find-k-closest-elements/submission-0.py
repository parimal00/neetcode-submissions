class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result =[]
        sorted_result=[]

        for n in arr:
            distance = n - x

            result.append([n, abs(distance)])
        

        result.sort(key=lambda x:x[1])

        for i in range(k):
            sorted_result.append(result[i][0])

        sorted_result.sort()

        return sorted_result

