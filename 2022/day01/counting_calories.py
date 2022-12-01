elves_supply_list = [0]
with open("input.txt") as calory_list:
    for item_calories in calory_list:
        if item_calories.rstrip():
            elves_supply_list[-1] += int(item_calories)
        else:
            elves_supply_list.append(0)
print(max(elves_supply_list))
elves_supply_list.sort()
print(sum(elves_supply_list[-3:]))
