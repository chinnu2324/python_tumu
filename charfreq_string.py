str = input('Enter the word:').lower()
dist_count = {}
for char in str:
    if char in dist_count:
        dist_count[char] += 1
    else:
        dist_count[char] = 1
print(dist_count)
for x,y in dist_count.items():
    print(f'{x}:{y}')
