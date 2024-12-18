#!/usr/bin/env python3

from io import StringIO
import sys
from contextlib import redirect_stdout


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
    global ip
    if A:
        ip = operand - 2
    return ip + 2


def bxc(operand):
    global B
    res = B ^ C
    B = res
    return res


def out(operand):
    res = combo(operand) & 0b111
    sys.stdout.write(f"{res},")
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


def run(program, verbose=False):
    global ip
    ip = 0
    while ip < len(program):
        ipv = f"{ip:02d}"
        opcode, operand = program[ip : ip + 2]
        res = op[opcode](operand)
        ip += 2
        if verbose:
            instr = f"{op[opcode].__name__} {operand:02d}"
            info = opinfo[opcode].format(
                literalop=f"{operand:02d}",
                comboop=comboinfo.get(operand, f"{operand:02d}"),
                res=f"{res:02d}",
            )
            print(f"\r{ipv}\t{instr}\t\t{info}")


def disassemble(program):
    header = "```\nASSUME\tCS:CODE\n\nCODE\tSEGMENT\nProgram:"
    body = "\n".join(
        f"\t{op[opcode].__name__} {operand:02d}"
        for opcode, operand in zip(program[::2], program[1::2])
    )
    footer = "CODE\tENDS\n\nEND\tProgram\n```"
    return f"{header}\n{body}\n{footer}"


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

opinfo = {
    0: "A <- A >> {comboop}\tA: {res}",
    1: "B <- B xor {literalop}\tB: {res}",
    2: "B <- {comboop} mod 08\tB: {res}",
    3: "A =/= 00?\tJMP {res}",
    4: "B <- B xor C\tB: {res}",
    5: "OUT {comboop} mod 08\tOUT {res}",
    6: "B <- A >> {comboop}\tB: {res}",
    7: "C <- A >> {comboop}\tC: {res}",
}
comboinfo = {
    4: "A",
    5: "B",
    6: "C",
}


def main(verbose=False):
    global A, B, C
    global ip
    with open("input.txt", "r") as fobj:
        A = int(next(fobj).rstrip().split(": ")[-1])
        B = B_init = int(next(fobj).rstrip().split(": ")[-1])
        C = C_init = int(next(fobj).rstrip().split(": ")[-1])
        next(fobj)
        program = tuple(map(int, next(fobj)[9:].split(",")))

    if verbose:
        print(disassemble(program), end="\n\n")
        print(f"Register A: {A}\nRegister B: {B}\nRegister C: {C}", end="\n\n")
    run(program, verbose)
    print("" if verbose else "\b ")

    A_copy = 0
    prg_ptr = -1
    while 0 > prg_ptr > -(len(program) + 1):
        A, B, C = A_copy, B_init, C_init
        with redirect_stdout(StringIO()) as output:
            run(program[:-2])
        out_ = int(output.getvalue().rstrip(","))
        if out_ == program[prg_ptr]:
            A_copy <<= 3
            prg_ptr -= 1
            continue
        if A_copy & 0b111 == 7:
            A_copy >>= 3
            prg_ptr += 1
        A_copy += 1
    print(A_copy >> 3 if prg_ptr else None)


if __name__ == "__main__":
    main(verbose=False)
