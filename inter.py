#!/usr/bin/env python
import sys


def intersect(fileset):
    fset = set(open(fileset[0]))
    for f in fileset[2:]:
        fd = open(f)
        fset &= set(fd)
    # print(list(fset))
    return fset


def main():
    try:
        inter = intersect(sys.argv[1:])
    except Exception as e:
        print(e)
        return
    for line in inter:
        print(line.strip())

if __name__ == '__main__':
    sys.exit(int(main() or 0))
