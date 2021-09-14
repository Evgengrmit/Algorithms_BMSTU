import sys
import re


input_file = sys.argv[1]
output_file = sys.argv[2]

summary = 0

with open(input_file, 'r') as read_f:
    for number in re.findall(r'-?\d+', read_f.read()):
        summary += int(number)

with open(output_file, 'w') as write_f:
    write_f.write(str(summary%256))
