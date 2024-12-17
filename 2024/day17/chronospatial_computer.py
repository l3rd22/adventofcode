#!/usr/bin/env python3


def adv(operand):
    global A
    res = A >> combo(operand)
    A = res
    return res


def bxl(operand):
    global B
    res = B ^ operand
    B = res
    return res


def bst(operand):
    global B
    res = combo(operand) & 0b111
    B = res
    return res


def jnz(operand):
    global instruction_pointer
    if not A:
        return
    instruction_pointer = operand - 2
    return operand


def bxc(operand):
    global B
    res = B ^ C
    B = res
    return res


def out(operand):
    res = combo(operand) & 0b111
    # print(f"{res},", end="")
    stdout.append(str(res))
    return res


def bdv(operand):
    global B
    res = A >> combo(operand)
    B = res
    return res


def cdv(operand):
    global C
    res = A >> combo(operand)
    C = res
    return res


def combo(operand):
    if operand in range(4):
        return operand
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    if operand == 7:
        raise ValueError


def disassemble(opcode, operand):
    instr = {
        0: "A <- A >> {combo_op} \t= {A:02d} >> {combo_operand:02d} \tA: {res:02d}",
        1: "B <- B xor {operand:02d} \t= {B:02d} xor {operand:02d} \tB: {res:02d}",
        2: "B <- {combo_op} mod 08 \t= {combo_operand:02d} mod 08 \tB: {res:02d}",
        3: "A != 00? \t{A:2d} != 00? \tGOTO {operand:02d}",
        4: "B <- B xor C \t= {B:02d} xor {C:02d} \tB: {res:02d}",
        5: "Out: {combo_op} mod 08 \t= {combo_operand:02d} mod 08 \tOut: {res:02d}",
        7: "C <- A >> {combo_op} \t= {A:02d} >> {combo_operand:02d} \tC: {res:02d}",
        6: "B <- A >> {combo_op} \t= {A:02d} >> {combo_operand:02d} \tB: {res:02d}",
    }
    combo_ops = {
        4: "A",
        5: "B",
        6: "C",
    }
    return instr[opcode].format(
        A=A,
        B=B,
        C=C,
        combo_op=combo_ops.get(operand, f"{operand:02d}"),
        operand=operand,
        combo_operand=combo(operand),
        res=op[opcode](operand),
    )


A, B, C = 0, 0, 0
instruction_pointer = 0
op = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}
stdout = []


def main(debug=False):
    global A, B, C
    global instruction_pointer
    with open("input.txt", "r") as fobj:
        A = int(next(fobj).rstrip().split(": ")[-1])
        B = int(next(fobj).rstrip().split(": ")[-1])
        C = int(next(fobj).rstrip().split(": ")[-1])
        next(fobj)
        program = tuple(map(int, next(fobj)[9:].split(",")))

    if debug:
        print("```\nASSUME\tCS:CODE\n\nCODE\tSEGMENT\nProgram:")
        for i in range(0, len(program), 2):
            print(f"\t{op[program[i]].__name__} {program[i+1]:02d}")
        print("CODE\tENDS\n\nEND\tProgram\n```\n")
        print(f"Register A: {A}\nRegister B: {B}\nRegister C: {C}\n")
        while instruction_pointer < len(program):
            opcode, operand = program[instruction_pointer : instruction_pointer + 2]
            print(f"{instruction_pointer:02d}:", end="\t")
            print(f"{op[opcode].__name__} {operand:02d}", end="\t\t")
            print(disassemble(opcode, operand))
            instruction_pointer += 2
        print("\nOut:", ",".join(stdout))

    else:
        while instruction_pointer < len(program):
            opcode, operand = program[instruction_pointer : instruction_pointer + 2]
            op[opcode](operand)
            instruction_pointer += 2
        print(",".join(stdout))

    ## Solved via manual DFS
    A, B, C = 0, 0, 0
    instruction_pointer = 0
    for num in (6, 5, 6, 2, 5, 5, 0, 4, 5, 4, 2, 5, 7, 1, 5, 5):
        A <<= 3
        A |= num
    print("\n", A)
    while instruction_pointer < len(program):
        opcode, operand = program[instruction_pointer : instruction_pointer + 2]
        op[opcode](operand)
        instruction_pointer += 2
    print("Out:", ",".join(stdout))
    print(program)

    # for init_val in (5,):  # range(8):
    #     print(init_val, end=": ")
    #     A = 0
    #     for num in (6, 5, 6, 2, 5, 5, 0, 4, 5, 4, 2, 5, 7, 1, 5):
    #         A |= num
    #         A = A << 3
    #     A |= init_val
    #     # 6, 5, 6, 2, 5, 5, 0|6, 4, 5|7, 4, 2, 5, 7, 0|1|2, 5, 5
    #     print(A)
    #     B = 0
    #     C = 0
    #     instruction_pointer = 0
    #     while instruction_pointer < len(program):
    #         opcode, operand = program[instruction_pointer : instruction_pointer + 2]
    #         op[opcode](operand)
    #         instruction_pointer += 2
    #     print()
    # print()


if __name__ == "__main__":
    main(debug=False)
