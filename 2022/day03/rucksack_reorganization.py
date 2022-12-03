def priority(item_type):
    if item_type.isupper():
        return ord(item_type) - ord("A") + 27
    return ord(item_type) - ord("a") + 1


sum_priorities = 0
possible_badges = ["a"]
sum_badge_priority = -1
with open("input.txt", "r") as content_list:
    for elf_number, rucksack in enumerate(r.rstrip() for r in content_list):
        first_compartment = set(rucksack[: len(rucksack) // 2])
        second_compartement = set(rucksack[len(rucksack) // 2 :])
        item_type = list(first_compartment & second_compartement)[0]
        sum_priorities += priority(item_type)

        if elf_number % 3:
            possible_badges = possible_badges & set(rucksack)
        else:
            sum_badge_priority += priority(list(possible_badges)[0])
            possible_badges = set(rucksack)
    sum_badge_priority += priority(list(possible_badges)[0])
print(sum_priorities)
print(sum_badge_priority)
