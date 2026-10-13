class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else: 
                frequency[num] = 1

        pq = []
        for num, freq in frequency.items():
            if len(pq) < k:
                heapq.heappush(pq, (freq, num))
            elif freq> pq[0][0]:
                heapq.heappop(pq)
                heapq.heappush(pq, (freq, num))
        res = []
        for freq, num in pq:
            res.append(num)
        return res
