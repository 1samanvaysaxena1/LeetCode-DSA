class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        dict1 = {}
        list1 = []
        for numbs in nums:
            if numbs in dict1:
                dict1[numbs] += 1
            else:
                dict1[numbs] = 1
        for number,frequency in dict1.items():
            heapq.heappush(heap,(frequency*(-1),number))
        for i in range(k):
            freq,number = heapq.heappop(heap)
            list1.append(number)
        return list1
