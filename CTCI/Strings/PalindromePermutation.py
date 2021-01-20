#Noman Ahmad
#Cracking the Coding Inerview
#Chapter 1: Arrays & Strings
#Problem 1.4: Palindrome Permutation: Given a string, write a function to
############# determine if it is a permutation of a palindrome.

#Solution 1: Hashing Approach
#Approach :  count the number of occurences of each character's in the string,
##########   at most there can be one odd number, the rest have to be even in
##########    order for it to be a permutation of a palindrome.
#Complexity: Time O(n), Space O(n)
def hashPalinPerm(str):
    str = str.lower()
    charHash = {}
    odd_repitions = 0
    for character in str:
        if character != ' ':
            if character in charHash:
                charHash[character] = charHash[character] + 1
            else:
                charHash[character] = 1

    for keys in charHash:
        if (charHash[keys] % 2 != 0):
            odd_repitions = odd_repitions + 1
    return (odd_repitions <= 1)


#Solution 2: ASCII Character Approach
#Approach: Similar to hashing but store repititions inside a ascii character array
#Complexity: Time O(n), Space O(1)
def asciiPalinPerm(str):
    str = str.lower()
    ascii_array = [0] * 128
    odd_repitions = 0
    for character in str:
        if character != ' ':
            ascii_value = ord(character)
            ascii_array[ascii_value] = ascii_array[ascii_value] + 1
    for i in range(0, 128, 1):
        if (ascii_array[i] % 2) != 0:
            odd_repitions = odd_repitions + 1
    return (odd_repitions <= 1)


#driver code
def main():
    input_string = input("Enter a string: ")
    isPerm = asciiPalinPerm(input_string)
    if (isPerm):
        print("The string " + input_string + " is a permutation of a palindrome.")
    else:
        print("The string " + input_string + " is not a permutation of a palindrome.")

#run the main function
if __name__ == "__main__":
    main()
