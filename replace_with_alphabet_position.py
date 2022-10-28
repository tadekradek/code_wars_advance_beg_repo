"""
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
Example

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

"""
#my_solution

def alphabet_position(text):
    key_lower = "abcdefghijklmnopqrstuvwxyz"
    key_upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join([str(key_lower.index(x)+1)+" " if x in key_lower else str(key_upper.index(x)+1)+" " if x in key_upper else "" for x in text]).rstrip()
   

#another solutions

#unicode based

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

text="rradek sergdtghdfs  314512"
[str(ord(c) - 96) for c in text.lower() if c.isalpha()]

"r".isalpha() # Return True if the string is an alphabetic string, False otherwise.
              # A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string. 

ord("R") # Return the Unicode code point for a one-character string.