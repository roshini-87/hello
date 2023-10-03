def MinWindowSubstring(strArr):
    N, K = strArr
    char_count_K = {}
    char_count_N = {}  
    min_window = ""
    min_length = float('inf')

    for char in K:
        char_count_K[char] = char_count_K.get(char, 0) + 1

    left, right = 0, 0

    while right < len(N):
        char = N[right]
        char_count_N[char] = char_count_N.get(char, 0) + 1

        while all(char_count_N.get(char, 0) >= count for char, count in char_count_K.items()):
            if right - left + 1 < min_length:
                min_window = N[left:right + 1]
                min_length = right - left + 1

            left_char = N[left]
            char_count_N[left_char] -= 1
            left += 1

        right += 1

    return min_window

strArr1 = ["aaabaaddae", "aed"]
strArr2 = ["aabdccdbcacd", "aad"]

result1 = MinWindowSubstring(strArr1)
result2 = MinWindowSubstring(strArr2)

print("Result 1:", result1)
print("Result 2:", result2)
