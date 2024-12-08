#!/usr/bin/env python3


def reverse_dfs(check, nums):
    if len(nums) == 0:
        return check == 0
    if check >= nums[-1]:
        if reverse_dfs(check - nums[-1], nums[:-1]):
            return True
    if check % nums[-1] == 0:
        if reverse_dfs(check // nums[-1], nums[:-1]):
            return True
    # # uncomment for part 2
    # if str(check)[1:].endswith(str(nums[-1])):
    #     return reverse_dfs(int(str(check)[: -len(str(nums[-1]))]), nums[:-1])
    return False


def main():
    with open("input.txt", "r") as fobj:
        print(
            sum(
                (
                    int(ls[0])
                    if reverse_dfs(
                        int((ls := line.split(": "))[0]),
                        list(map(int, ls[1].split(" "))),
                    )
                    else 0
                )
                for line in fobj
            )
        )


if __name__ == "__main__":
    main()
