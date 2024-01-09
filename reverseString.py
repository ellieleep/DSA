def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    while i != j:
        k = s[i]
        s[i] = s[j]
        s[j] = k
        i += 1
        j -= 1


reverseString(["h", "e", "l", "l", "o"])
