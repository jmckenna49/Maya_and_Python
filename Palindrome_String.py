def isPalindrome(s):
    newStr = ""
    for ch in s:
        if ch.isalnum():
            newStr+=ch.lower()
    return newStr == newStr[::-1]


if __name__ == "__main__":
    string = "racecar"
    pali = isPalindrome(string)
    output = str(pali)
    print(f" The string " + string + " is a palindrome: " + output)