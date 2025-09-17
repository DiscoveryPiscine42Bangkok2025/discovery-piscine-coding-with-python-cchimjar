import sys

def downcase_it(s):
    return s.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for x in sys.argv[1:]:
        print(downcase_it(x))