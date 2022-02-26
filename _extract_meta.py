from pathlib import Path
import os
import random
import json

random.seed(0)


def extract_meta(src: str) -> dict:
    _, cmd, _ = src.lstrip().split('"""', maxsplit=3)
    meta = {}
    for ln in cmd.splitlines():
        if ln.startswith("*"):
            parts = ln.strip("*").strip().split(":")
            if len(parts) > 1:
                key, value = parts
                meta[key] = int(value)
            else:
                meta[parts[0]] = 1
    return meta


def main():
    meta = {}
    folder = Path(__file__).parent

    for src in (folder / "answer").iterdir():
        if src.name.endswith(".py"):
            with open(src) as fd:
                data = extract_meta(fd.read())
                key = src.name.removesuffix(".py")
                meta[key] = data

    with open(folder / "meta.json", "w") as fd:
        json.dump(meta, fd)


if __name__ == "__main__":
    main()
