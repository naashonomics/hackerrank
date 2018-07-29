#Task : You have a test string . Your task is to match the string hackerrank. This is case sensitive.
#Note : This is a regex only challenge. You are not required to write code.  You only have to fill in the regex pattern in the blank (_________).

import re
Regex_Pattern = r'hackerrank'    # Do not delete 'r'.
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
