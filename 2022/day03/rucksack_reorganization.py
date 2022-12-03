sum_priorities = 0
possible_badges = ['a']
sum_badge_priority = -1
with open("input.txt", "r") as content_list:
    for elf_number, rucksack in enumerate(r.rstrip() for r in content_list):
        item_type = [itype for itype in rucksack[:len(rucksack)//2] if itype in rucksack[len(rucksack)//2:]][0]
        sum_priorities += (ord(item_type) - ord('A') + 27) if item_type.isupper() else (ord(item_type) - ord('a') + 1)

        if elf_number % 3:
            possible_badges = [itype for itype in possible_badges if itype in rucksack]
        else:
            sum_badge_priority += (ord(possible_badges[0]) - ord('A') + 27) if possible_badges[0].isupper() else (ord(possible_badges[0]) - ord('a') + 1)
            possible_badges = rucksack
    sum_badge_priority += (ord(possible_badges[0]) - ord('A') + 27) if possible_badges[0].isupper() else (ord(possible_badges[0]) - ord('a') + 1)
print(sum_priorities)
print(sum_badge_priority)
