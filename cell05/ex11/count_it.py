import sys

if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for x in sys.argv[1:]:
        print(f"{x}: {len(x)}")