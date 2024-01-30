import argparse
import re
from typing import List


def get_author(line: str):
    r_search = re.compile(r"\{([^}]+)\}$")
    match = r_search.search(line)
    if match:
        return match.group(1)
    else:
        return None


def get_current_entry(lines: iter):
    l = next(lines)
    l_stripped = l.strip()
    current_entry = ""
    if l_stripped.startswith("\\bibitem"):
        current_entry = l_stripped
        while current_entry.endswith("}"):
            l = next(lines)
            l_stripped = l.strip()
            current_entry += l_stripped
            if l_stripped.endswith("}"):
                break
    return current_entry


def wrapper(input: str, output: str):
    with open(input, "r") as fh:
        lines = iter(fh.readlines())

        list_of_authors: List[str] = []

        current_entry = ""
        for line in lines:
            if line.startswith("\\bibitem"):
                current_entry = line.strip()
                # print("1", current_entry)
                while not current_entry.endswith("}"):
                    line = next(lines)
                    # print("line", line)
                    current_entry += line.strip()
                    if current_entry.endswith("}"):
                        break
                # print("2", current_entry)
                matched_author = get_author(current_entry)
                if matched_author:
                    list_of_authors.append(matched_author)
            else:
                continue

        print(list_of_authors, len(list_of_authors))
        return list_of_authors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="argument", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
