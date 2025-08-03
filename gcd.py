def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcdOfStrings(str1, str2):
    # Check if both strings are made by repeating the same base
    if str1 + str2 != str2 + str1:
        return ""
    
    # Find GCD of lengths
    gcd_len = gcd(len(str1), len(str2))
    return str1[:gcd_len]

# ---- MAIN TEST CODE ----
if __name__ == "__main__":
    # Example input
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    
    result = gcdOfStrings(str1, str2)
    print("GCD of Strings:", result)
