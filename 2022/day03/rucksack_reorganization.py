sum_priorities = 0
with open("input.txt", "r") as content_list:
    for rucksack in (r.rstrip() for r in content_list):
        item_type = [itype for itype in rucksack[:len(rucksack)//2] if itype in rucksack[len(rucksack)//2:]][0]
        sum_priorities += (ord(item_type) - ord('A') + 27) if item_type.isupper() else (ord(item_type) - ord('a') + 1)
print(sum_priorities)
