
haystack = "leetcode"
needle = "leeto"

def strStr(haystack, needle):
    word= []
    for x in range(len(needle)):
        if haystack[x] == needle[x]:
            word.append(needle[x])
    if ''.join(word) == needle:
        return True
    else:
        return -1

print(strStr(haystack,needle))