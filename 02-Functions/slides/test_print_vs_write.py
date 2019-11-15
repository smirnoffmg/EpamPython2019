import os
import sys


ARG = sys.argv[1]

NAME = 'test_' + ARG
TEXT = 'test_message'

with open(NAME, 'w') as f:
    if ARG == 'print':
        for _ in range(10000000):
            print(TEXT, file=f)
    else:
        for _ in range(10000000):
            f.write(TEXT+'\n')
    f.flush()

os.remove(NAME)

# time python test_print_vs_write.py print
# time python test_print_vs_write.py write