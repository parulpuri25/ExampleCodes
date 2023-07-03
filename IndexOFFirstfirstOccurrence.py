#Given two strings s1 and s2, return the index of the first occurrence of s1 in s2, or -1 if s1 is not part of s2.
def firstOccurrence(s1,s2):
    if s1 in s2:
        return s2.index(s1)
    else:
        return -1


firstOccurrence('nee','needle')
