'''
Anagram Check
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
'''

def check_anagram(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()
    return sorted(string1) == sorted(string2)

def check_anagram_method2(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()
    # anagrams should have same length
    if len(string1) != len(string2):
        return False
    counter = {}
    # count the frequencies of the first string...
    for i in string1:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    # check the second string and decrease the count by 1 if found
    for i in string2:
        if i in counter:
            counter[i] -= 1
        else:
            counter[i] = 1
    for i in counter:
        if counter[i] != 0:
            return False
    return True

def check_anagram_method3(string1, string2):
    string1 = string1.replace(' ','').lower()
    string2 = string2.replace(' ','').lower()
    if len(string1) != len(string2):
        return False
    sum1 = 0
    for i in string1:
        sum1 += ord(i)
    sum2 = 0
    for i in string2:
        sum2 += ord(i)
    return sum1 == sum2