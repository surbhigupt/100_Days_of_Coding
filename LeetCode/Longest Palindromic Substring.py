def longestPalindrome(self, s):
        ## Idea: odd length palins
        ## - - - - - - - - - - - - (input)
        ##           ^
        ##           |
        ##           i              current pointer
        ##  left<-(j) (k)->right   
        ## move j and k until s[j] == s[k] or j>=0 and k<len(s)
        
        ## Idea: even length palins
        ## - - - - - -  - - - - - - (input)
        ##           ^  ^
        ##           |  |
        ##           i i+1             current pointer
        ##  left<-(j)     (k)->right   
        ## move j and k until s[j] == s[k] or j>=0 and k<len(s)
        
        length = len(s)
        
        def expand_center(i, j):
            
            ## The pointer i moves towards the left and the pointer j moves towards the right
            
            while i >= 0 and j < len(s) and s[i] == s[j]:
                
                i -= 1
                j += 1 ## same speed for both and move opposite
                
            return s[i + 1 : j]
        
        result = ''     
        
        for i in range(length):
            ## odd length palindromes centered at i
            temp_palin = expand_center(i, i) 
            
            if len(temp_palin) > len(result):
                result = temp_palin
                
            if i + 1 < len(s):
                ## even length palindromes centered around i, i+1
                temp_palin = expand_center(i, i + 1) 
                
                if len(temp_palin) > len(result):
                    result = temp_palin    
                    
        return result