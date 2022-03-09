#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
from subprocess import run, STDOUT, PIPE
import subprocess
from unidecode import unidecode


def execute(script: str, inputs: str) -> str:
    subprocess
    cmd = [sys.executable, script]
    inputs = unidecode(inputs) + "\n"
    res = subprocess.run(cmd, input=inputs, stdout=PIPE, stderr=PIPE, text=True)
    if res.stderr:
        print(inputs.strip())
        print("---")
        print(res.stderr)
        raise RuntimeError
    out = unidecode(res.stdout)
    print(inputs.strip())
    print(out.strip())
    print("---")
    return out


def main():
    for path in (Path(__file__).parent / "tests").iterdir():
        s_path = str(path)
        if s_path.endswith(".input"):
            print("\n" + path.name.upper())
            script_name = path.name.removesuffix(".input") + ".py"
            script = path.parent.parent / "answer" / script_name

            with open(path) as fd:
                examples = map(lambda x: x + "\n", fd.read().split("\n---\n"))

            outputs = [execute(script, example) for example in examples]
            with open(s_path.removesuffix(".input") + ".output", "w") as fd:
                fd.write("---\n".join(outputs))


if __name__ == "__main__":
    main()
