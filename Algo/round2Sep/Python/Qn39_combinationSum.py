class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(current, sums):
            # if sums > target:
            #     val = current.pop()
            #     sums -= val
            #     return 
            # if sums == target:
            #     temp = current.copy()
            #     temp.sort()
            #     if temp not in result:
            #         result.append(temp)
            #     val = current.pop()
            #     sums -= val
            #     return 
            
            for val in candidates:
                sums += val
                if sums > target: 
                    sums -= val
                elif sums == target:
                    current.append(val)
                    temp = current.copy()
                    temp.sort()
                    if temp not in result:
                        result.append(temp)
                    current.pop()
                    sums -= val
                else:
                    current.append(val)
                    dfs(current, sums)
                    current.pop() # vital line. must pop after each recursion call so that you backtrack properly
                    sums -= val

        current = []
        sums = 0
        dfs(current, sums)

        return result
        

