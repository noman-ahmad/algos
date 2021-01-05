#Noman Ahmad
#Cracking the Coding Interview
#Chapter 1: Arrays & Strings
#Problem 1.1: Is Unique: Implement an algorithm to determine if a string has all
############# unique characters. What if you cannot use additional data structures?

#Solution 1 : Brute Force Approach
#Approach   : For every character in string check if it exists elsewhere in string.
#Complexity : Time -> O(n^2), Space -> O(1) where n = length of string
def isUniqueBruteForce(str):
    unique_string = True
    for i, character_i in enumerate(str):
        for j, character_j in enumerate(str):
            if ((i != j) and (character_i == character_j)):
                unique_string = False
                break
    return unique_string

#Solution 2 : Hash Table Solution (Uses Data Structure)
#Approach   : if any repeated character is found from hash table, return false
#Complexity : Time -> O(n), Space -> O(n) where n = length of string
def isUniqueHash(str):
    unique_string = True
    charHash = set()
    for character in str:
        if character in charHash:
            unique_string = False
            break
        else:
            charHash.add(character)
    return unique_string


#Solution 3 : Sorting (No Data Structure)
#Approach   : Sort the String in-place, then check adjacent elements
#Complexity : Time -> O(nlogn), Space -> O(1) if sorted in-place, n = length of String
def isUniqueSort(str):
    unique_string = True
    str = sorted(str)
    n = len(str)
    for i in range(0, n-1):
        current_char = str[i]
        next_char = str[i+1]
        if current_char == next_char:
            unique_string = False
    return unique_string

#Solution 4 : ASCII Boolean Array (Solution Provided in Book)
#Approach   : keep a boolean array for all 128 ascii characters, and if they are
############  ever values who's array value is true, we return false
#Complxity  : Time -> O(n) [really a lot less O(128)], Space -> O(1), n = length of String
def isUniqueAscii(str):
    unique_string = True
    if len(str) > 128:
        unique_string = False
    else:
        #initialize 128 length array to false
        char_check = [False] * 128
        for char in str:
            ascii_value = ord(char)
            if char_check[ascii_value] == True:
                unique_string = False
                break
            else:
                char_check[ascii_value] = True
    return unique_string


# Driver Code
def main():
    input_string = input("Enter a String: ")
    uniqueness = isUniqueAscii(input_string)
    if (uniqueness):
        print("The String " + input_string + " has all unique characters")
    else :
        print("The String " + input_string + " does not have all unique characters")


# Run Main Faction
if __name__ == "__main__":
    main()
