#!/usr/bin/env python3

from io import StringIO
import sys
from contextlib import redirect_stdout


def adv(operand, verbose=False):
    global A
    res = A >> combo(operand)
    A = res
    if verbose:
        sys.stdout.write(
            f"A <- A >> {combo_verbose.get(operand, f'{operand:02d}')}\tA: {res:02d}"
        )
    return res


def bxl(operand, verbose=False):
    global B
    res = B ^ operand
    B = res
    if verbose:
        sys.stdout.write(f"B <- B xor {operand:02d}\tB: {res:02d}")
    return res


def bst(operand, verbose=False):
    global B
    res = combo(operand) & 0b111
    B = res
    if verbose:
        sys.stdout.write(
            f"B <- {combo_verbose.get(operand, f'{operand:02d}')} mod 08\tB: {res:02d}"
        )
    return res


def jnz(operand, verbose=False):
    global ip
    if not A:
        if verbose:
            sys.stdout.write("A =/= 00?\tNOP")
        return ip + 2
    ip = operand - 2
    if verbose:
        sys.stdout.write(f"A =/= 00?\tJMP {operand:02d}")
    return operand


def bxc(operand, verbose=False):
    global B
    res = B ^ C
    B = res
    if verbose:
        sys.stdout.write(f"B <- B xor C\tB: {res:02d}")
    return res


def out(operand, verbose=False):
    res = combo(operand) & 0b111
    if verbose:
        sys.stdout.write(
            f"OUT {combo_verbose.get(operand, f'{operand:02d}')} mod 08\tOUT {res:02d}"
        )
    else:
        sys.stdout.write(f"{res},")
    return res


def bdv(operand, verbose=False):
    global B
    res = A >> combo(operand)
    B = res
    if verbose:
        sys.stdout.write(
            f"B <- A >> {combo_verbose.get(operand, f'{operand:02d}')}\tB: {res:02d}"
        )
    return res


def cdv(operand, verbose=False):
    global C
    res = A >> combo(operand)
    C = res
    if verbose:
        sys.stdout.write(
            f"C <- A >> {combo_verbose.get(operand, f'{operand:02d}')}\tC: {res:02d}"
        )
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
        opcode, operand = program[ip : ip + 2]
        if verbose:
            print(
                f"\n{ip:02d}\t{op[opcode].__name__} {operand:02d}",
                end="\t\t",
            )
        op[opcode](operand, verbose)
        ip += 2


def disassemble(program):
    header = "```\nASSUME\tCS:CODE\n\nCODE\tSEGMENT\nProgram:"
    body = "\n".join(
        f"\t{op[opcode].__name__} {operand:02d}"
        for opcode, operand in zip(program[::2], program[1::2])
    )
    footer = "CODE\tENDS\n\nEND\tProgram\n```"
    return f"{header}\n{body}\n{footer}"


combo_verbose = {
    4: "A",
    5: "B",
    6: "C",
}
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
        print(f"Register A: {A}\nRegister B: {B}\nRegister C: {C}")
    run(program, verbose)
    print("\n" if verbose else "\b ")

    program_str = ",".join(map(str, program))
    A_copy = 0
    while A_copy < (1 << 3 * len(program)):
        A, B, C = A_copy, B_init, C_init
        with redirect_stdout(StringIO()) as output:
            run(program)
        output_str = output.getvalue().rstrip(",")
        if output_str == program_str:
            break
        if program_str.endswith(output_str):
            A_copy <<= 3
            continue
        if A_copy & 0b111 == 7:
            A_copy >>= 3
        A_copy += 1
    print(A_copy)


if __name__ == "__main__":
    main(verbose=False)
