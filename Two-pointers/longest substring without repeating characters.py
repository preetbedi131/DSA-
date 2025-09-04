 seen = set()
        max_len = 0
        left = 0 
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len = max(max_len, right-left+1)  # length of the window right-left+1
        return max_len
        
