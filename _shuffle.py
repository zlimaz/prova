#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
import os
import random
import unidecode

random.seed(0)


def transform_line(st: str):
    st = st.strip()
    if st.startswith("#") and not st.endswith("."):
        st = st.strip(" #")
    st = unidecode.unidecode(st)
    return st


def transform(src: str) -> str:
    _, cmd, code = src.lstrip().split('"""', maxsplit=3)
    lines = sorted(filter(None, map(transform_line, code.splitlines())))

    while lines and lines[-1].endswith(":"):
        ln = lines.pop()
        lines.insert(random.randrange(len(lines)), ln)

    for i, ln in enumerate(lines):
        if ln.endswith(":"):
            for j in range(i + 1, len(lines)):
                lines[j] = "    " + lines[j]

    result = ['"""', cmd.strip(), '"""', "", *lines]
    return "\n".join(result)


def main():
    for src in (Path(__file__).parent / "answer").iterdir():
        if src.name.endswith(".py"):
            dest = src.parent.parent / src.name
            print(f"{dest.name=}")
            with open(src, encoding="utf-8") as fd:
                data = transform(fd.read())
            with open(dest, "w", encoding="utf-8") as fd:
                fd.write("# -*- coding: utf-8 -*-\n")
                fd.write(data)


if __name__ == "__main__":
    main()
