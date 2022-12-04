containing_assignments = 0
overlapping_assignments = 0
with open("input.txt") as assignment_list:
    for elf1, elf2 in (line.rstrip().split(",") for line in assignment_list):
        elf1 = list(map(int, elf1.split("-")))
        elf2 = list(map(int, elf2.split("-")))
        if ((elf1[0]-elf2[0])*(elf1[1]-elf2[1])) <= 0:
            containing_assignments += 1
        if ((elf1[0]-elf2[1])*(elf1[1]-elf2[0])) <= 0:
            overlapping_assignments += 1
print(containing_assignments)
print(overlapping_assignments)

