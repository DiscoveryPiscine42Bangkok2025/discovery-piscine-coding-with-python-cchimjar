import sys

if len(sys.argv) != 3:
    print("none")
else:
    x = sys.argv[1]
    y = sys.argv[2]
    count = y.count(x)
    if count == 0:
        print("none")
    else:
        print(count)