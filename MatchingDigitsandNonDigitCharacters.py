#Task You have a test string . Your task is to match the pattern  xxXxxXxxxx Here  denotes a digit character, and  denotes a non-digit character.
import re
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, input()))).lower())
