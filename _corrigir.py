#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from pathlib import Path
from subprocess import STDOUT, PIPE
import subprocess
import json
import os
import sys


def indent(st):
    return "\n".join("    " + ln for ln in st.splitlines())


def error(inpt, out, expect, empty="*none*"):
    return "\n".join(
        [
            "Input:",
            indent(inpt or empty),
            "Output:",
            indent(out or empty),
            "Expect:",
            indent(expect or empty),
        ]
    )


def check(script: str, inputs: str, expect) -> str:
    try:
        compile(open(script, encoding="utf-8").read(), script, "exec")
    except SyntaxError:
        return "Compilation error: not valid Python code!"

    cmd = [sys.executable, script]
    res = subprocess.run(cmd, input=inputs.encode("utf8"), stdout=PIPE, stderr=PIPE)
    if res.stderr:
        return error(inputs, res.stderr.decode("utf8"), expect)
    elif not res.stdout and not expect.strip():
        return None
    elif not res.stdout:
        return error(inputs, "", expect)
    elif (out := res.stdout.decode("utf8")).strip() == expect.strip():
        return None
    else:
        return error(inputs, out, expect)


def main():
    root = Path(__file__).parent
    if not (g_path := root / "grades.json").exists():
        grades = {}
    else:
        grades = json.load(g_path.open())

    valid_paths = [p.removesuffix(".py") for p in sys.argv[1:]]
    filter_paths = bool(valid_paths)
    has_errors = False

    for path in (root / "tests").iterdir():
        if not path.name.endswith(".input"):
            continue
        name = path.name.removesuffix(".input")

        if filter_paths and name not in valid_paths:
            continue
        elif filter_paths:
            valid_paths.remove(name)

        with open(path, encoding="utf-8") as fd:
            examples = fd.read().split("---\n")

        out_path = path.parent / (name + ".output")
        with open(out_path, encoding="utf-8") as fd:
            results = fd.read().split("\n---")
        script = path.parent.parent / (name + ".py")

        errors = []
        for (ex, out) in zip(examples, results):
            err = check(script, ex, out)
            if err:
                has_errors = True
                errors.append(err)

        if errors:
            print(f"\n\nERROR: {os.path.basename(path)}")
            for error in errors:
                print(error)
            grades[name] = False
        else:
            grades[name] = True

    if valid_paths:
        not_found = ", ".join(valid_paths)
        print(f"ERRO: Exercício(s) não encontrado: {not_found}")
    elif not has_errors:
        print("SUCESSO: Correção concluída sem encontrar erros")

    g_path.write_text(json.dumps(grades), encoding="utf-8")


if __name__ == "__main__":
    main()
