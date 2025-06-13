"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

from collections import Counter

def canConstruct(ransomNote,magazine):
    st1, st2 = Counter(ransomNote), Counter(magazine)
    # Counter({'a': 2}) == Counter({'a': 2}) → True
    if st1 & st2 == st1:
        return True
    return False

canConstruct('aa', 'aab')