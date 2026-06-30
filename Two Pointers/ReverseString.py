"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character."""

from typing import List

"""
## Solution - using two pointers implementations

Steps 
- Read the list of string using one pointer from the beginning of the list and other from the end.
- Swap the elements -><-
- then move both pointer in their respective directions.
- repeat that until pointers cross each other.

Complexity:
 This implementation iterates throught the string once - time complexity : O(n)
 Doesn't use any extra storage to save string data or create new: space complexity : O(1)
"""


# Code
def reverseString(s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

#s = ["h","e","l","l","o"]
#s = ["H","a","n","n","a","h"]
s = ["o","l","l","e","h"]

reverseString(s)
for chr in s:
    print(chr)