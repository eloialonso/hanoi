"""
Recursive implementation of Hanoi Towers game.
"""


def main():
    n = int(input("Number of disks : "))
    hanoi(n, "1", "2", "3")


def hanoi(n, start, aux, end):
    assert n >= 1, f"Impossible to play with {n} disk."
    if n == 1:
        print_instruction(start, end)
        return
    hanoi(n - 1, start, end, aux)
    print_instruction(start, end)
    hanoi(n - 1, aux, end, start)


def print_instruction(start, end):
    print(f"Take the disk on tower {bcolors.BOLD}{bcolors.OKGREEN}{start}{bcolors.ENDC} and place it on tower {bcolors.BOLD}{bcolors.OKBLUE}{end}{bcolors.ENDC}", end="")
    input(" (press any key to continue)")


# from: https://stackoverflow.com/a/287944
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


if __name__ == "__main__":
    main()
