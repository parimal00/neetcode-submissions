class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer=0

        if len(word1) > len(word2):
            small_word=word2
            large_word=word1
        else:
            small_word=word1
            large_word=word2
        
        result=""
        while pointer<len(small_word):
            result+=word1[pointer]
            result+=word2[pointer]
            pointer+=1

        return result + large_word[pointer:len(large_word)]
        # return result


        