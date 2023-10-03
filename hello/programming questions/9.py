def longest_common_prefix(strings):
    if not strings:
        return ""
    strings.sort()
    
    first_str = strings[0]
    last_str = strings[-1]
    min_len = min(len(first_str), len(last_str))
    common_prefix = ""

    for i in range(min_len):
        if first_str[i] == last_str[i]:
            common_prefix += first_str[i]
        else:
            break

    return common_prefix

A = ["ab","ac","adf","abcd"]
result = longest_common_prefix(A)
print("Longest common prefix:", result)
