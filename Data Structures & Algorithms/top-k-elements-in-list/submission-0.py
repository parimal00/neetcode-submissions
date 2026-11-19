class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for n in nums:
            hashmap[n] = hashmap.get(n,0) + 1

        data = list(hashmap.items())
        data.sort(key=lambda x:x[1], reverse=True)
        res=[]
        for i in range(k):
            res.append(data[i][0])

        return res

        