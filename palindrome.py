def ispalindrome(word):
    #base case 1: empty strings are palindromes 
    if not word: #a more efficient version of it len(word)==0:
        return true
    #base case 2 : a single string
    elif len(word)==1:
        return true 
    #base case 3: two or three charachters
    elif len(word)<=3:
        return word[0]==word[-1] #if first and last letter are the same then its a palindrome
    else:
        #we have a complicated long word
        #Solution 1 compare if the reversed version is equal to the original 
        flipped=word[::-1] #to reverse a sclicable obj in python
        #altinative way to write this is : flipped = " ".join(reversed(word))
        return word==flipped

        #Solution 3: compare the ends togather
        i = 0
        j = len(word)-1
        while i<j:
            if word[i]!=word[j]:
                return false
            i+=1 #i++
            j+=1 #j++

