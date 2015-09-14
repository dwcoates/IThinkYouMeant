def binarySearch(dictionary, anagram)
    found = False
    beginning = 0
    end = len(dictionary)-1
    
    while beginning <= end and not word:
        middle = (beginning + end)//2
            if dictionary[middle] == anagram:
                found = True
            else:
                if anagram < dictionary[middle]:
                    end = middle-1
                else:
                    beginning = middle+1
    return word
