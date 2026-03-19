class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        if(len(word1) < len(word2)):
            target = len(word1)
            dummy = word2
        elif(len(word1) == len(word2)):
            target = len(word1)
            dummy = False
        else:
            target = len(word2)
            dummy = word1
        
        result = ""
        
        for i in range(target):
            result = "".join([result, word1[i], word2[i]])
        
        if dummy:
            result = "".join([result, dummy[i+1:]])
        
        return result
            

if __name__ == "__main__":
    s = Solution()
    word1 = input()
    word2 = input()
    print(s.mergeAlternately(word1, word2))
            

        

        