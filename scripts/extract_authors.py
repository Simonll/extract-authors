import argparse
import re
from typing import List


def wrapper(input: str, output: str):
    rx_t = re.compile(r"""(?<!\\)%.+|(\\(?:no)?citet?\{((?!\*)[^{}]+)\})""")
    rx_p = re.compile(r"""(?<!\\)%.+|(\\(?:no)?citep?\{((?!\*)[^{}]+)\})""")
    with open(input, "r") as fh:
        lines = fh.readlines()
        print(lines)
        list_of_authors: List[str] = []
        for l in lines:
            list_of_authors += [
                m.group(2).split(",") for m in rx_t.finditer(l) if m.group(2)
            ]
            list_of_authors += [
                m.group(2).split(",") for m in rx_p.finditer(l) if m.group(2)
            ]

        list_of_authors = [a for group_of_a in list_of_authors for a in group_of_a]
        list_of_authors = list(set(list_of_authors))

        print(list_of_authors, len(list_of_authors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="argument", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
