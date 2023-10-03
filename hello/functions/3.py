def divide_string(s, k):
    n = len(s)
    
    # Check if it's possible to create k fragments
    if k > n:
        return None
    
    # Calculate the approximate size of each fragment
    fragment_size = n // k
    
    fragments = []
    current_fragment = ""
    
    for char in s:
        current_fragment += char
        
        # Check if the current fragment has unique characters
        if len(set(current_fragment)) == len(current_fragment):
            fragments.append(current_fragment)
            current_fragment = ""
    
    # If there are leftover characters in the last fragment, add it
    if current_fragment:
        fragments.append(current_fragment)
    
    # If the number of fragments is not equal to k, return None
    if len(fragments) != k:
        return None
    
    return fragments

# Example usage:
s = "aabdddddcghssas"
k = 3
fragments = divide_string(s, k)
if fragments:
    print(fragments)
else:
    print("Cannot divide the string into k fragments with unique characters.")
