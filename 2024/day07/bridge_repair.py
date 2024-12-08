#!/usr/bin/env python3


def dfs(nums, check):
    if len(nums) == 1:
        return nums[0] == check
    if nums[0] > check:
        return False
    if not dfs([nums[0] + nums[1], *nums[2:]], check):
        return dfs([nums[0] * nums[1], *nums[2:]], check)
    return True


def main():
    with open("input.txt", "r") as fobj:
        print(
            sum(
                (
                    int(line.split(": ")[0])
                    if dfs(
                        list(map(int, line.split(": ")[1].split(" "))),
                        int(line.split(": ")[0]),
                    )
                    else 0
                )
                for line in fobj
            )
        )


if __name__ == "__main__":
    main()
