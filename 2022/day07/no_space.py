def process_command(line, pointer):
    cmd = line.rstrip("\n").split(" ")
    match cmd[1]:
        case "cd":
            update_pointer(cmd[2], pointer)
        case "ls":
            pass


def update_pointer(dest, pointer):
    match dest:
        case "/":
            pointer = [0]
        case "..":
            pointer.pop()
        case _:
            for idx, content in enumerate(get_cwd(filesystem, pointer)):
                if not isinstance(content, list):
                    continue
                if content[0] == dest:
                    pointer.append(idx)
                    break


def get_cwd(filesystem, pointer):
    cwd = filesystem
    for idx in pointer:
        cwd = cwd[idx]
    return cwd


def update_contents(line, filesystem, pointer):
    if line.startswith("dir"):
        get_cwd(filesystem, pointer).append([line.rstrip("\n").split(" ")[1], ])
    else:
        size, name = line.rstrip("\n").split(" ")
        get_cwd(filesystem, pointer).append((name, int(size)))


def update_dirs(filesystem, dirs):
    size = 0
    for content in filesystem:
        if isinstance(content, tuple):
            size += content[1]
        if isinstance(content, list):
            _, dirsize = update_dirs(content, dirs)
            size += dirsize
    dirs.append((filesystem[0], size))
    return (filesystem[0], size)



filesystem = [["/", ]]
pointer = [0]
with open("input.txt") as terminal_output:
    for line in terminal_output:
        if line.startswith("$"):
            process_command(line, pointer)
        else:
            update_contents(line, filesystem, pointer)
dirs = []
update_dirs(filesystem[0], dirs)
print(sum(d[1] for d in dirs if d[1] <= 100_000))
dirnames, dirsizes = zip(*dirs)
required_space = 30_000_000 - (70_000_000 - dirsizes[dirnames.index("/")])
print(min(size for size in dirsizes if size >= required_space))