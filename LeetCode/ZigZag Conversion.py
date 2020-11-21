class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or not s or len(s)<2 :
            return s
        
        list_index = []
        step_size = 2*numRows-2
        n = numRows - 1

        k = 0
        while k < len(s):
            list_index.append(k)
            k = k + step_size
        
        for i in range(1, numRows-1):
            mid_step = 2*n-2
            j = i
            mid_list = []
            while j < len(s):
                mid_list.append(j)
                mid_list.append(j+mid_step)
                j = j + step_size
            list_index = list_index + [x for x in mid_list if x<len(s)]
            n = n - 1

        k = numRows-1
        while k < len(s):
            list_index.append(k)
            k = k + step_size
        
        return ''.join([s[idx] for idx in list_index])  