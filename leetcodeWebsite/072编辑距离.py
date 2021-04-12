from functools import lru_cache

@lru_cache(maxsize=None, typed=False)
def Levenshtein_Distance_Recursive(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1 == str2:
        return 0

    if str1[len(str1) - 1] == str2[len(str2) - 1]:
        d = 0
    else:
        d = 1

    return min(Levenshtein_Distance_Recursive(str1, str2[:-1]) + 1,
               Levenshtein_Distance_Recursive(str1[:-1], str2) + 1,
               Levenshtein_Distance_Recursive(str1[:-1], str2[:-1]) + d)


print(Levenshtein_Distance_Recursive("abc", "bd"))
