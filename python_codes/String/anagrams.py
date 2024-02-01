# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:50:13 2024

@author: admin
"""
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters in both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")

