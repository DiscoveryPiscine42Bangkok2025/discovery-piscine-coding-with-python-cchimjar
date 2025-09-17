import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        j = 0
        row = []
        while j <= 10:
            row.append(str(i * j))
            j += 1
        print(f"Table de {i}: {' '.join(row)}")
        i += 1