""" 
    Given a string s, return true if it is a palindrome, or false otherwise.
   
    - A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
    it reads the same forward and backward. 
    - Alphanumeric characters include letters and numbers.
    
    -  Example 1:
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.
    
    - Example 2:
        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.
    
    - Example 3:
        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.
   
     Constraints:
        1 <= s.length <= 2 * 105
        s consists only of printable ASCII characters.
"""

## Solution - using two pointers implementations
"""
Steps 
- Read the string using one pointer from the beginning of the string and other from the end.
- Check if its alphanumeric character if not then we move the pointer point at non aplhanumeric char
    - forward or backward depending on the pointer/value.
- Check if two pointers are pointing at indeces with same char after converting char to lowercase 
    then move both pointer in their respective directions.
- repeat that until pointer cross each other.
- if the char doesn't match then return False else return True.

Complexity:
 This implementation iterates throught the string once - time complexity : O(n)
 Doesn't use any extra storage to save string data or create new: space complexity : O(1)
""" 

def isPalindrome(s: str) -> bool:

    leftPointer = 0
    rightPointer = len(s) - 1

    while leftPointer < rightPointer:
        while leftPointer < rightPointer and not s[leftPointer].isalnum():
            leftPointer += 1
        while leftPointer < rightPointer and not s[rightPointer].isalnum():
            rightPointer -= 1
        
        if s[leftPointer].lower() != s[rightPointer].lower():
            return False

        leftPointer += 1
        rightPointer -= 1
    
    return True

#s = " "
#s = "race a car"
s = "AmanaplanacanalPanama"
#s = "A man, a plan, a canal: Panama"
#s = "tab a cat"
print(isPalindrome(s))