import re
import sys

test_string = input()
regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.
match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
