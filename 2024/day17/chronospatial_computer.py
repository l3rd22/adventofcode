#!/usr/bin/env python3 -O

from io import StringIO
from contextlib import redirect_stdout


def adv(operand):
    global A
    A = A >> combo(operand)


def bxl(operand):
    global B
    B = B ^ operand


def bst(operand):
    global B
    B = combo(operand) & 0b111


def jnz(operand):
    global ip
    if A != 0:
        ip = operand - 2


def bxc(operand):
    global B
    B = B ^ C


def out(operand):
    res = combo(operand) & 0b111
    print(res, end=",")


def bdv(operand):
    global B
    B = A >> combo(operand)


def cdv(operand):
    global C
    C = A >> combo(operand)


def combo(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7:
            raise ValueError


instruction = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}


def run(program):
    global ip
    ip = 0
    while ip < len(program):
        opcode, operand = program[ip : ip + 2]
        instruction[opcode](operand)
        ip += 2


def disassemble(program):
    instr_info = {
        0: "A RSHIFT {comboop}\tSTORE A",
        1: "B XOR {literalop}\tSTORE B",
        2: "{comboop} MOD 08\tSTORE B",
        3: "IF A NEQ 00\tJUMP {literalop}",
        4: "B XOR C\tSTORE B",
        5: "{comboop} MOD 08\tOUTPUT",
        6: "A RSHIFT {comboop}\tSTORE B",
        7: "A RSHIFT {comboop}\tSTORE C",
    }
    code = []
    for opcode, operand in zip(program[::2], program[1::2]):
        lop = f"{operand:02d}"
        cop = {4: "A", 5: "B", 6: "C"}.get(operand, lop)
        code.append(
            f"\t{instruction[opcode].__name__} {lop}\t\t; "
            + instr_info[opcode].format(literalop=lop, comboop=cop)
        )
    return "\n".join(code)


def debug(program):
    global ip
    suffix = {
        0: "{A}",
        1: "{B}",
        2: "{B}",
        3: "",
        4: "{B}",
        5: "{out}",
        6: "{B}",
        7: "{C}",
    }
    output = StringIO()
    ip = 0
    while ip < len(program):
        print(f"{ip:02d}", end="")
        opcode, operand = prog = program[ip : ip + 2]
        print(disassemble(prog), end="\t")
        with redirect_stdout(StringIO()) as stream:
            instruction[opcode](operand)
        output.write(out_ := stream.getvalue())
        ip += 2
        print(suffix[opcode].format(A=A, B=B, C=C, out=out_.rstrip(",")))
    print("\nOutput:", output.getvalue().rstrip(","))


def main():
    global A, B, C
    with open("input.txt", "r") as fobj:
        A = int(next(fobj).rstrip().split(": ")[-1])
        B = B_init = int(next(fobj).rstrip().split(": ")[-1])
        C = C_init = int(next(fobj).rstrip().split(": ")[-1])
        next(fobj)
        program = tuple(map(int, next(fobj)[9:].split(",")))

    if __debug__:
        print("```\nmain:\n", disassemble(program), "\n```", end="\n\n")
        print(f"Register A: {A}\nRegister B: {B}\nRegister C: {C}", end="\n\n")
        debug(program)
    else:
        run(program)
    print("\b ")

    A_init = 0
    prg_ptr = -1
    while 0 > prg_ptr > -(len(program) + 1):
        A, B, C = A_init, B_init, C_init
        with redirect_stdout(StringIO()) as output:
            run(program[:-2])
        out_ = int(output.getvalue().rstrip(","))
        if out_ == program[prg_ptr]:
            A_init <<= 3
            prg_ptr -= 1
            continue
        if A_init & 0b111 == 7:
            A_init >>= 3
            prg_ptr += 1
        A_init += 1
    print(A_init >> 3 if prg_ptr else None)


if __name__ == "__main__":
    main()
