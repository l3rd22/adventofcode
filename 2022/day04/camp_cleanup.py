with open("input.txt") as assignment_list:
    print(
        sum(
            (elf1[0] - elf2[0]) * (elf1[1] - elf2[1]) <= 0
            for elf1, elf2 in (
                map(lambda elf: list(map(int, elf.split("-"))), elf_tuple)
                for elf_tuple in (line.rstrip().split(",") for line in assignment_list)
            )
        )
    )

with open("input.txt") as assignment_list:
    print(
        sum(
            (elf1[0] - elf2[1]) * (elf1[1] - elf2[0]) <= 0
            for elf1, elf2 in (
                map(lambda elf: list(map(int, elf.split("-"))), elf_tuple)
                for elf_tuple in (line.rstrip().split(",") for line in assignment_list)
            )
        )
    )
