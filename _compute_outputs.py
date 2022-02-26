import os
import sys
from pathlib import Path
from subprocess import run, STDOUT, PIPE
import subprocess


def execute(script: str, inputs: str) -> str:
    subprocess
    cmd = [sys.executable, script]
    stdin = inputs.encode("utf8") + b"\n"
    res = subprocess.run(cmd, input=stdin, stdout=PIPE, stderr=PIPE)
    if res.stderr:
        print(inputs)
        print("---")
        print(res.stderr.decode("utf8"))
        raise RuntimeError
    out = res.stdout.decode("utf8")
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
