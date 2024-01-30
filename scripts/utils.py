import os


def extract_key(bibtex_entry):
    # Find the start and end of the key
    start = bibtex_entry.find("{") + 1
    end = bibtex_entry.find(",")

    # Extract and return the key
    if start != -1 and end != -1:
        return bibtex_entry[start:end]
    else:
        return None


def generate_bib(input, output, list_of_authors):
    os.makedirs(os.path.dirname(output), exist_ok=True)

    with open(input, "r") as f:
        lines = iter(f.readlines())

        for line in lines:
            if line.strip().startswith("@"):
                key = extract_key(line.strip())

                if key in list_of_authors:
                    list_of_lines = []
                    list_of_lines += [line]
                    while not line.startswith("}"):
                        line = next(lines)
                        list_of_lines += [line]
                        if line.startswith("}"):
                            with open(output, "a") as o:
                                for l in list_of_lines:
                                    o.write(l)
                            break
                else:
                    continue

            else:
                continue
