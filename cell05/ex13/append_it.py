import sys

if len(sys.argv) == 1:
    print("none")
else:
    for x in sys.argv[1:]:
        if not x.endswith("ism"):
            print(x + "ism")