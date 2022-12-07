def collect(dict_, dname, dir_):
    total_size = 0
    for name, size in dir_.items():
        if isinstance(size, dict):
            total_size += collect(dict_, f"{dname}/{name}", size)[0]
        else:
            total_size += size
    dict_[dname] = total_size
    return total_size, dict_




cwd = [{}]
with open("input.txt") as terminal_output:
    for line in terminal_output:
        match line.rstrip().split():
            case ["$", "cd", "/"]:
                cwd = [cwd[0]]
            case ["$", "cd", ".."]:
                if len(cwd) > 1:
                    cwd.pop()
            case ["$", "cd", dir_]:
                cwd.append(cwd[-1].setdefault(dir_, {}))
            case ["$", "ls"]:
                continue
            case ["dir", _]:
                continue
            case [size, fname]:
                cwd[-1][fname] = int(size)
dir_sizes = collect({}, "/", cwd[0])[1]
print(sum(size for size in dir_sizes.values() if size <= 100_000))
print(min(size for size in dir_sizes.values() if size >= 30_000_000 - (70_000_000 - dir_sizes["/"])))

