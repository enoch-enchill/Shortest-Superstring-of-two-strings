def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def longestSubstringFinder(string1, string2):
    answer = ""
    var1, var2 = string1, string2
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""

    if var2.index(answer) == 0:
        return var1 + remove_prefix(var2, answer)
    else:
        return var2 +  remove_prefix(var1, answer)


print (longestSubstringFinder("greed", "eddy"))
