#!/usr/bin/env python3
import sys


def intersect(fileset):
    fset = set(open(fileset[0]).readlines())
    for f in fileset[2:]:
        fd = open(f)
        fset &= set(fd.readlines())
    # print(list(fset))
    return fset


def main():
    try:
        inter = intersect(sys.argv[1:])
    except Exception as e:
        print(e)
        return
    for line in list(inter):
        print(line,end="")

if __name__ == '__main__':
    sys.exit(int(main() or 0))
