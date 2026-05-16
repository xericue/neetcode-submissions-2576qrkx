class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {}

        # map numbers to their frequencies
        for i in nums:
            f_map[i] = f_map.get(i, 0) + 1
        
        # based on their frequencies, return the elements with the highest ones
            
        arr = []

        for key, val in f_map.items():
            arr.append([val, key])
        
        arr.sort()
        
        ret_arr = []

        while len(ret_arr) < k:
            ret_arr.append(arr.pop()[1])
            
        return ret_arr