"""
Recursive implementation of Hanoi Towers game.
"""


import argparse
from functools import partial


def main():
    args = parse_args()
    n = args.nb_disks if args.nb_disks is not None else ask_for_nb_disks(args.language)
    assert n >= 1
    print_fn = partial(print_instruction, wait=args.interactive, language=args.language)
    hanoi(n, "1", "2", "3", print_fn)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nb-disks", type=int, default=None, help="Number of disks.")
    parser.add_argument("-i", "--interactive", action="store_true", help="Print all the moves without waiting for user input between the moves.")
    parser.add_argument("-l", "--language", choices=["en", "fr"], type=str, default="en", help="Language.")
    return parser.parse_args()


def ask_for_nb_disks(language):
    if language == "en":
        prompt = "Number of disks: "
        impossible = "Invalid input."
    elif language == "fr":
        prompt = "Nombre de disques: "
        impossible = "Entrée invalide."
    while True:
        n = input(prompt)
        if not n.isdigit() or int(n) < 1:
            print(impossible)
            continue
        return int(n)


def hanoi(n, start, aux, end, print_fn):
    if n == 1:
        print_fn(start, end)
        return
    hanoi(n - 1, start, end, aux, print_fn)
    print_fn(start, end)
    hanoi(n - 1, aux, end, start, print_fn)


def print_instruction(start, end, wait=True, language="en"):
    if language == "en":
        instruction = f"Take the disk on tower {bcolors.BOLD}{bcolors.OKGREEN}{start}{bcolors.ENDC} and place it on tower {bcolors.BOLD}{bcolors.OKBLUE}{end}{bcolors.ENDC}"
        continue_prompt = " (press any key to continue)"
    elif language == "fr":
        instruction = f"Prendre le disque sur la tour {bcolors.BOLD}{bcolors.OKGREEN}{start}{bcolors.ENDC} et le placer sur la tour {bcolors.BOLD}{bcolors.OKBLUE}{end}{bcolors.ENDC}"
        continue_prompt = " (appuyer sur n'importe quelle touche pour continuer)"
    else:
        raise AssertionError(f"Unsupported language: {language}") 
    print(instruction, end="" if wait else "\n")
    if wait:
        input(continue_prompt)


# from: https://stackoverflow.com/a/287944
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


if __name__ == "__main__":
    main()
