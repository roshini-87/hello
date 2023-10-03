def generate_sublists(L, N):
    if N > len(L) or N <= 0:
        return []

    def backtrack(start, curr_sublist):
        if len(curr_sublist) == N:
            sublists.append(curr_sublist[:])
            return
        for i in range(start, -1, -1):
            curr_sublist.append(L[i])
            backtrack(i - 1, curr_sublist)
            curr_sublist.pop()

    sublists = []
    backtrack(len(L) - 1, [])
    return sublists

# Example usage:
L = [1, 2, 3, 4]
N = 3
result = generate_sublists(L, N)

# Print the result
for sublist in result:
    print(sublist)
