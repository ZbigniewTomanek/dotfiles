#!/bin/python3

from argparse import ArgumentParser
from pathlib import Path
import os


parser = ArgumentParser()
parser.add_argument("rel", type=str)
parser.add_argument("tgt", type=str)


def create_symlink(rel_str, tgt_str):
    rel = Path(rel_str)
    tgt = Path(tgt_str)

    local = tgt.relative_to(rel)
    os.makedirs(local.parent, exist_ok=True)
    local_str = local.as_posix()

    os.system(f"ln {tgt_str} {local_str}")


if __name__ == "__main__":
    args = parser.parse_args()
    create_symlink(args.rel, args.tgt)






