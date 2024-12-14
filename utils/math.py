from collections.abc import Sequence


def gcd(*integers: int) -> tuple[int, ...]:
    """Greatest common divisor and Bézout coefficients.

    Compute the greatest common divisor of the specified integer
    arguments and coefficients satisfying Bézout's identity using the
    extended Euclidean algorithm.

    Args:
        *integers: Variable number of integer arguments.

    Returns:
        Greatest common divisor and Bézout coefficients. If all
        arguments are zero, then the returned divisor and coefficients
        are all ``0``. ``gcd()`` without arguments returns ``(0,)``.

    Raises:
        TypeError: If any of the arguments is not an ``int``.
    """
    if len(integers) == 0:
        return (0,)
    for i, a in enumerate(integers):
        if not isinstance(a, int):
            raise TypeError(
                f"'{type(a).__name__}' object cannot be interpreted as an integer"
            )
        if i == 0:
            r0, bezout = a, [1 * (a != 0)]
            continue
        r1 = a
        s0, s1 = 1, 0
        t0, t1 = 0, 1
        while r1:
            q = r0 // r1
            r0, r1 = r1, r0 - q * r1
            s0, s1 = s1, s0 - q * s1
            t0, t1 = t1, t0 - q * t1
        bezout = [*(bez * s0 for bez in bezout), t0]
    if r0 < 0:
        return -r0, *(-bez for bez in bezout)
    return r0, *bezout


def invmod(a: int | Sequence[int], m: int, /) -> int | tuple[int, ...]:
    r"""Modular multiplicative inverse.

    Compute modular multiplicative inverse x that satisfies

    .. math::
    
        a x \equiv 1 \quad (\mathrm{mod}\ m) \,.

    If multiple integers :math:`a_i` are specified, then the inverses
    :math:`x_i` satisfying

    .. math::

        a_1 x_1 \equiv 1 \quad (\mathrm{mod}\ m) \\
        a_2 x_2 \equiv 1 \quad (\mathrm{mod}\ m) \\
        \vdots

    are returned.

    Args:
        a: Integer argument. Multiple values can be specified.
        m: Common modulus.

    Returns:
        Modular multiplicative inverse. For multiple integers, a tuple
        of the inverses is returned.

    Raises:
        TypeError: If any of the arguments is not an ``int``.
        ValueError: If the modular multiplicative inverse for any of the
            integers `a` in mod `m` does not exist.
    """
    if isinstance(a, int):
        g, x, _ = gcd(a, m)
        if g != 1:
            raise ValueError(f"modular multiplicative inverse does not exist")
        return x
    b = [1]
    for ai in a:
        if not isinstance(ai, int):
            raise TypeError(
                f"'{type(ai).__name__}' object cannot be interpreted as an integer"
            )
        b.append((ai * b[-1]) % m)
    print(b)
    g, invb, _ = gcd(b[-1], m)
    if g != 1:
        raise ValueError(f"modular multiplicative inverse does not exist")
    x = []
    for ai, bi in zip(a[::-1], b[-2::-1]):
        x.append((invb * bi) % m)
        invb = (invb * ai) % m
    print(x)
    return (*x[::-1],)
