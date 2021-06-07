'''
    189. Most Common Word
    https://leetcode.com/problems/most-common-word/
    
'''

import re 
import operator
from collections import defaultdict

class Solution(object):

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        splitParagraph = re.split(r'\W+', paragraph.lower())
        wordCount = defaultdict(int)
        
        bannedWords = set(banned)
        
        for word in splitParagraph:
            if word not in bannedWords:
                wordCount[word] +=1
        
        return max(wordCount.items(), key=operator.itemgetter(1))[0]
    
    
    def mostCommonWordList(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        splitParagraph = re.split(r'\W+', paragraph.lower())
        
        notBannedWords = []
        for word in splitParagraph:
            if word not in banned:
                notBannedWords.append(word)
        
        return max(notBannedWords, key=notBannedWords.count)


most = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']
word = most.mostCommonWord(paragraph, banned)
print(word)

wordAux = most.mostCommonWordList(paragraph, banned)
print(word)