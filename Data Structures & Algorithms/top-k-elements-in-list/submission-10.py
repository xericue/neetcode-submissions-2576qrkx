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
        
        arr.sort(reverse=True)
        
        ret_arr = []

        for i in arr:
            if len(ret_arr) == k:
                break
            ret_arr.append(i[1])

        return ret_arr