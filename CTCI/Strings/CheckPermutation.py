# Noman Ahmad
# Cracking the Coding Interview
# Chapter 1:    Arrays & Strings
# Problem 1.2 : Given 2 Strings, write a method to decide if one is a permutation
##############  of the other.

# Solution 1 : Brute Force
# Approach   : Check if Character Occurs Same # of Times in both arrays
# Complexity : Time -> O(n^2), Space -> O(1)
# note       : non-equally sized strings cant be permutations of each other
def checkPermutationBrute(str1, str2):
    are_permutations = True
    if len(str1) != len(str2):
        are_permutations = False
    else:
        for characters in str1:
            first_string_occurences = 0;
            second_string_occurences = 0;
            for first_char in str1:
                if characters == first_char:
                    first_string_occurences = first_string_occurences + 1
            for second_char in str2:
                if characters == second_char:
                    second_string_occurences = second_string_occurences + 1
            if first_string_occurences != second_string_occurences:
                are_permutations = False
                break
    return are_permutations


# Solution 2  : Sorting
# Approach    : Sort Both Strings And Check if the Sorted Strings Are Equal
# Complexity  : Time -> O(nlogn), Space -> O(1) if sorted in-place, where n is
##############  the length of the strings.
# note         : Non-Equally Sized Strings can't be permutations of each other
def checkPermutationSort(str1, str2):
    are_permutations = True
    if len(str1) != len(str2):
        are_permutations = False
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        if str1 != str2:
            are_permutations = False
    return are_permutations

# Solution 3 : Hashing
# Approach   : Insert all of s1 characters into hash table, check for s2
# Complexity : Time -> O(n), Space -> O(n), where n is the length of the strings.
# Note       : Non-Equally Sized Strings can't be permutations of each other.
def checkPermutationHash(str1, str2):
    are_permutations = True
    if len(str1) != len(str2):
        are_permutations = False
    else:
        # this dict will hold (char,number of occurences) key,value pairs
        occurenceHash = dict()
        for char in str1:
            if char in occurenceHash:
                occurenceHash[char] = occurenceHash[char] + 1
            else:
                occurenceHash[char] = 1
        for char in str2:
            if char in occurenceHash:
                occurenceHash[char] = occurenceHash[char] - 1
            else:
                are_permutations = False
                break
        if are_permutations:
            for key in occurenceHash:
                if occurenceHash[key] != 0:
                    are_permutations = False
                    break
    return are_permutations


# Solution : Ascii Boolean Array
# Approach : Create 2 Ascii Arrays of size 128, one to hold true/false, one to
###########  to hold the number of occurences. check for str2
# Complexity : Time -> O(n), Space -> O(1)
#note        : Non-Equally Sized Strings cant be permutations of each other
def checkPermutationAscii(str1, str2):
    are_permutations = True
    if len(str1) != len(str2):
        are_permutations = False
    else:
        #initialize the boolean "checking" arrays
        char_check = [False] * 128
        occurence_check = [0] * 128
        # determine character occurences from first strings
        for character in str1:
            ascii_value = ord(character)
            if char_check[ascii_value] == False:
                char_check[ascii_value] = True
            occurence_check[ascii_value] = occurence_check[ascii_value] + 1
            # compare characters in string2 from occurences in string 1
        for character in str2:
            ascii_value = ord(character)
            if char_check[ascii_value] == False:
                are_permutations = False
                break
            else:
                occurence_check[ascii_value] = occurence_check[ascii_value] - 1
        # perform final occurences check for extra or less elements in string 2
        if are_permutations:
            for vals in occurence_check:
                if vals != 0:
                    are_permutations = False
                    break
        return are_permutations


# driver code
def main():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    permutations = checkPermutationAscii(str1, str2)
    if (permutations):
        print(str1 + " and " + str2 + " are permutations of each other")
    else:
        print(str1 + " and " + str2 + " are not permutations of each other")
# call main
if __name__ == "__main__":
    main()
