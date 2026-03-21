class Solution:
    def gcdOfStrings_euclid(self, str1: str, str2: str) -> str: 
        
        if str1 + str2 != str2+str1: # The key is that is they are made up of the same pattern, adding them in these 2 ways gives the same result.
            return ""
        
        def gcd(a,b): # Euclid algorithm!
            while b:
                a, b = b, a % b
            return a
        
        result = gcd(len(str1), len(str2))
        return str1[:result]
    
                

        
    
    def gcdOfStrings_bruteforce(self, str1: str, str2: str) -> str: 
        len1 = len(str1)
        len2 = len(str2)
        i = 1
        output = ""

        while i <= len1 and i <= len2:
            if len1 % i != 0 or len2 % i != 0:
                i += 1
                continue
            
            # check if it is common
            if str2[:i] != str1[:i]:
                i += 1
                continue
            
            s = str1[:i]
            
            flag1 = (s*(len1//i) == str1)
            flag2 = (s*(len2//i) == str2)

            if flag1 and flag2:
                output = s
            
            i += 1
        return output

            

            
        
            
            



        
