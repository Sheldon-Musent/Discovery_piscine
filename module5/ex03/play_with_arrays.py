arr = [2, 8, 9, 48, 8, 22, -12, 2]
set = {10, 11, 50, 24}

print(arr)
print("{" + ", ".join (str(x) for x in sorted(set)) + "}") 

# ", ".join (map(str, set))