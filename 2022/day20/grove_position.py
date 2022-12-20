decryption_key = 811_589_153  # 1  # part one
with open("input.txt", "r") as puzzle_input:
    sequence = list(map(lambda s: int(s) * decryption_key, puzzle_input))
indices = list(range(len(sequence)))
for _ in range(10):  # 1 # part one
    for i, number in enumerate(sequence):
        old_index = indices[i]
        new_index = (old_index + number - 1) % (len(sequence) - 1) + 1
        indices = [
            index
            + ((index - old_index) * (new_index - index) >= 0)
            * (-1) ** (new_index > old_index)
            for index in indices
        ]
        indices[i] = new_index
decrypted_sequence = [number for _, number in sorted(zip(indices, sequence))]
print(
    sum(
        decrypted_sequence[
            (decrypted_sequence.index(0) + offset) % len(decrypted_sequence)
        ]
        for offset in (1000, 2000, 3000)
    )
)
