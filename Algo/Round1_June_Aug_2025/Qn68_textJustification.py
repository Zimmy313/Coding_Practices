from typing import *

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]: # no optimal. can be improved by a constant number of operations
        # done so by not adding " " while appending to the list.
        
        result = []
        temp = []
        counter = maxWidth
        for word in words:
            n = len(word)
            if n <= counter: # greedily add new word
                temp.append(word + " ")
                counter -= n+1
            
            else: # cannot add anymore. start processing into result
                last_word = temp.pop()
                last_word = last_word.rstrip()
                temp.append(last_word)
                
                total = sum(len(w) for w in temp)
                difference = maxWidth - total 
                
                if total == maxWidth:
                    temp_sentence = "".join(temp)
                    result.append(temp_sentence)
                
                else:
                    if len(temp) == 1:
                        temp[0] = temp[0].ljust(maxWidth)
                    
                    else:
                        last_word = temp.pop()
                        for i in range(difference):
                            index = i % len(temp)
                            temp[index] = temp[index] + " "
                        
                        temp.append(last_word)
                        
                    temp_sentence = "".join(temp)
                    result.append(temp_sentence)
                
                # resetting
                temp = [word+" "]
                counter = maxWidth - len(word) - 1
        
        # re-process the final sentence
        if not temp: # temp is empty
            last_sentence = result.pop()
            temp = last_sentence.split()
            last_sentence = " ".join(temp)
            last_sentence = last_sentence.ljust(maxWidth)
            result.append(last_sentence)
        else:
            last_sentence = "".join(temp)
            temp = last_sentence.split()
            last_sentence = " ".join(temp)
            last_sentence = last_sentence.ljust(maxWidth)
            result.append(last_sentence)
            

        
        return result 

if __name__ == "__main__":
    s = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(s.fullJustify(words, maxWidth ))
                
                
                
                    
                    