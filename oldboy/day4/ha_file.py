import re
with open(r'haporxy.conf') as file:
    for line in enumerate(file.readlines()):
        if 'buy.oldboy.org' in line:
            print number