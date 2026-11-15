class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [[temp, idx], [temp, idx]]

        # keep removing items from stack until their temp is less than 
        # output is index of curr_temp_idx - stack_temp_idx at the idx of output_idx[stack_temp]

        temp_stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while temp_stack and temp_stack[-1][0] < temp:
                top_temp = temp_stack.pop()
                res[top_temp[1]] = idx - top_temp[1]
 
            temp_stack.append([temp, idx])
        
        return res